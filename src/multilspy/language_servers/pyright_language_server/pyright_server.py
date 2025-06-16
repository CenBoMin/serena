"""
Provides Python specific instantiation of the LanguageServer class. Contains various configurations and settings specific to Python.
"""

import asyncio
import json
import logging
import os
import pathlib
import re
from contextlib import asynccontextmanager
from typing import AsyncIterator, Tuple

from overrides import override

from multilspy.multilspy_logger import MultilspyLogger
from multilspy.language_server import LanguageServer
from multilspy.lsp_protocol_handler.server import ProcessLaunchInfo
from multilspy.lsp_protocol_handler.lsp_types import InitializeParams
from multilspy.multilspy_config import MultilspyConfig


class PyrightServer(LanguageServer):
    """
    Provides Python specific instantiation of the LanguageServer class using Pyright.
    Contains various configurations and settings specific to Python.
    """
    def __init__(self, config: MultilspyConfig, logger: MultilspyLogger, repository_root_path: str):
        """
        Creates a PyrightServer instance. This class is not meant to be instantiated directly.
        Use LanguageServer.create() instead.
        """
        super().__init__(
            config,
            logger,
            repository_root_path,
            # Note 1: we can also use `pyright-langserver --stdio` but it requires pyright to be installed with npm
            # Note 2: we can also use `bpyright-langserver --stdio` if we ever are unhappy with pyright
            ProcessLaunchInfo(cmd="python -m pyright.langserver --stdio", cwd=repository_root_path),
            "python",
        )
        
        # Event to signal when initial workspace analysis is complete
        self.analysis_complete = asyncio.Event()
        self.found_source_files = False

    @override
    def is_ignored_dirname(self, dirname: str) -> bool:
        return super().is_ignored_dirname(dirname) or dirname in ["venv", "__pycache__"]

    def _get_initialize_params(self, repository_absolute_path: str) -> InitializeParams:
        """
        Returns the initialize params for the Pyright Language Server.
        """
        # Create basic initialization parameters
        initialize_params: InitializeParams = { # type: ignore
            "processId": os.getpid(),
            "rootPath": repository_absolute_path,
            "rootUri": pathlib.Path(repository_absolute_path).as_uri(),
            "initializationOptions": {
                "exclude": [
                    "**/__pycache__",
                    "**/.venv",
                    "**/.env",
                    "**/build",
                    "**/dist",
                    "**/.pixi",
                ],
                "reportMissingImports": "error",
            },
            "capabilities": {
                "workspace": {
                    "applyEdit": True,
                    "workspaceEdit": {"documentChanges": True},
                    "didChangeConfiguration": {"dynamicRegistration": True},
                    "didChangeWatchedFiles": {"dynamicRegistration": True},
                    "symbol": {
                        "dynamicRegistration": True,
                        "symbolKind": {
                            "valueSet": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
                        },
                    },
                    "executeCommand": {"dynamicRegistration": True},
                },
                "textDocument": {
                    "synchronization": {"dynamicRegistration": True, "willSave": True, "willSaveWaitUntil": True, "didSave": True},
                    "completion": {
                        "dynamicRegistration": True,
                        "contextSupport": True,
                        "completionItem": {
                            "snippetSupport": True,
                            "commitCharactersSupport": True,
                            "documentationFormat": ["markdown", "plaintext"],
                            "deprecatedSupport": True,
                            "preselectSupport": True,
                        },
                        "completionItemKind": {
                            "valueSet": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
                        },
                    },
                    "hover": {"dynamicRegistration": True, "contentFormat": ["markdown", "plaintext"]},
                    "signatureHelp": {
                        "dynamicRegistration": True,
                        "signatureInformation": {
                            "documentationFormat": ["markdown", "plaintext"],
                            "parameterInformation": {"labelOffsetSupport": True},
                        },
                    },
                    "definition": {"dynamicRegistration": True},
                    "references": {"dynamicRegistration": True},
                    "documentHighlight": {"dynamicRegistration": True},
                    "documentSymbol": {
                        "dynamicRegistration": True,
                        "symbolKind": {
                            "valueSet": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
                        },
                        "hierarchicalDocumentSymbolSupport": True,
                    },
                    "codeAction": {
                        "dynamicRegistration": True,
                        "codeActionLiteralSupport": {
                            "codeActionKind": {
                                "valueSet": [
                                    "",
                                    "quickfix",
                                    "refactor",
                                    "refactor.extract",
                                    "refactor.inline",
                                    "refactor.rewrite",
                                    "source",
                                    "source.organizeImports",
                                ]
                            }
                        },
                    },
                    "codeLens": {"dynamicRegistration": True},
                    "formatting": {"dynamicRegistration": True},
                    "rangeFormatting": {"dynamicRegistration": True},
                    "onTypeFormatting": {"dynamicRegistration": True},
                    "rename": {"dynamicRegistration": True},
                    "typeHierarchy": {"dynamicRegistration": True},
                    "publishDiagnostics": {"relatedInformation": True},
                },
            },
            "workspaceFolders": [
                {"uri": pathlib.Path(repository_absolute_path).as_uri(), "name": os.path.basename(repository_absolute_path)}
            ],
        }

        return initialize_params

    @asynccontextmanager
    async def start_server(self) -> AsyncIterator["PyrightServer"]:
        """
        Starts the Pyright Language Server and waits for initial workspace analysis to complete.
        
        This prevents zombie processes by ensuring Pyright has finished its initial background
        tasks before we consider the server ready.

        Usage:
        ```
        async with lsp.start_server():
            # LanguageServer has been initialized and workspace analysis is complete
            await lsp.request_definition(...)
            await lsp.request_references(...)
            # Shutdown the LanguageServer on exit from scope
        # LanguageServer has been shutdown cleanly
        ```
        """

        async def execute_client_command_handler(params):
            return []

        async def do_nothing(params):
            return

        async def window_log_message(msg):
            """
            Monitor Pyright's log messages to detect when initial analysis is complete.
            Pyright logs "Found X source files" when it finishes scanning the workspace.
            """
            message_text = msg.get("message", "")
            self.logger.log(f"LSP: window/logMessage: {message_text}", logging.INFO)
            
            # Look for "Found X source files" which indicates workspace scanning is complete
            # Unfortunately, pyright is unreliable and there seems to be no better way
            if re.search(r"Found \d+ source files?", message_text):
                self.logger.log("Pyright workspace scanning complete", logging.INFO)
                self.found_source_files = True
                self.analysis_complete.set()
                self.completions_available.set()

        async def check_experimental_status(params):
            """
            Also listen for experimental/serverStatus as a backup signal
            """
            if params.get("quiescent") == True:
                self.logger.log("Received experimental/serverStatus with quiescent=true", logging.INFO)
                if not self.found_source_files:
                    self.analysis_complete.set()
                    self.completions_available.set()

        # Set up notification handlers
        self.server.on_request("client/registerCapability", do_nothing)
        self.server.on_notification("language/status", do_nothing)
        self.server.on_notification("window/logMessage", window_log_message)
        self.server.on_request("workspace/executeClientCommand", execute_client_command_handler)
        self.server.on_notification("$/progress", do_nothing)
        self.server.on_notification("textDocument/publishDiagnostics", do_nothing)
        self.server.on_notification("language/actionableNotification", do_nothing)
        self.server.on_notification("experimental/serverStatus", check_experimental_status)

        async with super().start_server():
            self.logger.log("Starting pyright-langserver server process", logging.INFO)
            await self.server.start()

            # Send proper initialization parameters
            initialize_params = self._get_initialize_params(self.repository_root_path)

            self.logger.log(
                "Sending initialize request from LSP client to pyright server and awaiting response",
                logging.INFO,
            )
            init_response = await self.server.send.initialize(initialize_params)
            self.logger.log(f"Received initialize response from pyright server: {init_response}", logging.INFO)

            # Verify that the server supports our required features
            assert "textDocumentSync" in init_response["capabilities"]
            assert "completionProvider" in init_response["capabilities"]
            assert "definitionProvider" in init_response["capabilities"]

            # Complete the initialization handshake
            self.server.notify.initialized({})
            
            # Wait for Pyright to complete its initial workspace analysis
            # This prevents zombie processes by ensuring background tasks finish
            self.logger.log("Waiting for Pyright to complete initial workspace analysis...", logging.INFO)
            try:
                await asyncio.wait_for(self.analysis_complete.wait(), timeout=1.0)
                self.logger.log("Pyright initial analysis complete, server ready", logging.INFO)
            except asyncio.TimeoutError:
                self.logger.log("Timeout waiting for Pyright analysis completion, proceeding anyway", logging.WARNING)
                # Fallback: assume analysis is complete after timeout
                self.analysis_complete.set()
                self.completions_available.set()

            yield self

    @override
    def _supports_lsp_type_hierarchy(self) -> bool:
        """Pyright does not support LSP 3.17 type hierarchy methods."""
        return False

    @override
    def _is_inheriting_from(self, file_path: str, class_symbol: dict, target_class_name: str) -> bool:
        """
        Check if a Python class symbol is inheriting from the target class.
        This is a heuristic check that reads the source code around the class definition.
        """
        try:
            # Read the line where the class is defined
            abs_path = os.path.join(self.repository_root_path, file_path)
            if not os.path.exists(abs_path):
                return False
                
            with open(abs_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            class_range = class_symbol.get("range", {})
            start_line = class_range.get("start", {}).get("line", -1)
            
            if start_line < 0 or start_line >= len(lines):
                return False
            
            # Check the class definition line for inheritance
            class_line = lines[start_line].strip()
            
            # Look for patterns like "class Child(Parent):" or "class Child(Base, Parent):"
            if f"({target_class_name}" in class_line or f", {target_class_name}" in class_line or f"{target_class_name})" in class_line:
                return True
                
            # Also check a few lines after in case the inheritance spans multiple lines
            for i in range(start_line + 1, min(start_line + 3, len(lines))):
                line = lines[i].strip()
                if line.endswith("):") or line.endswith(","):
                    if target_class_name in line:
                        return True
                else:
                    break  # Stop if we hit a line that doesn't look like continuation
                    
            return False
            
        except Exception as e:
            self.logger.log(f"Error checking inheritance in {file_path}: {e}", logging.DEBUG)
            return False