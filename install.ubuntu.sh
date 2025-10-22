#!/bin/bash

INSTALL_DIR="/usr/local/bin"

install_util() {
    echo "[ status   ] Installing $UTILITY_NAME to $INSTALL_DIR"

    chmod +x "./$UTILITY_NAME"

    if command -v sudo &> /dev/null; then
        sudo cp "./$UTILITY_NAME" "$INSTALL_DIR/"
    else
        cp "./$UTILITY_NAME" "$INSTALL_DIR/"
    fi
}

check_installation_status() {
    if [ "$1" -eq 0 ]; then
        echo "[ success  ] $UTILITY_NAME installation is successful"
    else
        echo "[ failure  ] $UTILITY_NAME installation failed. You might need sudo or root access."
        exit 1
    fi
}


chmod +x install.dependencies.ubuntu.sh
sudo ./install.dependencies.ubuntu.sh

UTILITY_NAME="src/audio.multiplier.py"
install_util
check_installation_status $?

UTILITY_NAME="src/audio.multiplier"
install_util
check_installation_status $?

