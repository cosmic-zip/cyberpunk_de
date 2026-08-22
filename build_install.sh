#!/bin/bash
set -e

# Install the system dependencies
bash install.sh

# Ensure the Tauri CLI is installed
cargo install tauri-cli --features tauri-runtime-wry

# Build the frontend single page application
python3 build.py build

# Build the Tauri application
cd src-tauri
cargo tauri build
