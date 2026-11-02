# Developer Machine Setup

This guide covers the initial setup of a developer machine, including folder structure, software installation, command-line tools, Python, package managers, and development environments.

## 1. Folder Structure Setup

Create a dedicated folder for development projects.

* **D Drive:** Create a development folder directly.
* **C Drive:** Alternatively, create the folder inside the C drive.

Example:

```text
D:/
 └── Developer/
     ├── Projects/
     ├── Python/
     ├── Web-Development/
     └── Tools/
```

## 2. Download and Install Software

Software can be installed in two ways:

* **GUI (Graphical User Interface):** Installing software using graphical interfaces.
* **Non-GUI (Command Line Interface):** Installing software using terminal commands.

## 3. Windows Shells

Windows provides different shells to execute commands.

* **Command Prompt (CMD):** Traditional Windows command-line shell.
* **PowerShell:** Modern command-line shell with advanced administration capabilities.

### Important PowerShell Commands

| Command        | Description                    |
| -------------- | ------------------------------ |
| `New-Item`     | Creates files and folders      |
| `Get-Location` | Displays the current directory |
| `Set-Location` | Changes the current directory  |
| `Remove-Item`  | Deletes files and folders      |
| `Get-TimeZone` | Displays the system time zone  |

**Note:** Press `TAB` to automatically complete commands, file names, and folder paths.

## 4. Windows Terminal

Windows Terminal is an application that allows developers to access multiple command-line interfaces (CLIs) in one place.

* Windows 11: Generally available by default.
* Windows 10: Can be installed through the Microsoft Store.

## 5. Visual Studio Code

Visual Studio Code (VS Code) is a popular code editor used for software development.

### Recommended Extensions

* VSCode Icons – Improves file and folder identification.
* Additional extensions can be installed based on development requirements.

## 6. Python Installation

Install Python version **3.13**.

### Windows Installation

Open PowerShell or Windows Terminal and execute:

```powershell
winget install -e --id Python.Python.3.13
```

### Verify Python Installation

```powershell
python --version
```

### Pip – Python Package Manager

Pip is the default package manager for installing and managing Python packages and libraries.

## 7. UV – Python Package Manager

UV is a fast Python package and project manager.

It helps developers:

* Install Python dependencies.
* Manage Python libraries.
* Create and manage virtual environments.
* Manage project dependencies.

## 8. Package Managers

### Windows – Winget

Winget is the Windows Package Manager used to install, update, upgrade, and uninstall software through command-line instructions.

Useful resources:

* [Winget](https://learn.microsoft.com/en-us/windows/package-manager/winget/)
* [Winget.run](https://winget.run/)
* [Winstall](https://winstall.app/)

### macOS – Homebrew

Homebrew is a package manager for macOS that simplifies software installation through terminal commands.

**Install Homebrew:**

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

**Install Visual Studio Code:**

```bash
brew install --cask visual-studio-code
```

**Install Python 3.13:**

```bash
brew install python@3.13
```

**Install UV:**

```bash
brew install uv
```

## 9. Next Steps

After completing the developer machine setup, proceed with:

1. Cloud account creation.
2. Cloud CLI installation and configuration.
3. Git installation and setup.
4. GitHub account configuration.
5. Project creation and source code management.

---

**Goal:** Prepare a developer machine with all the essential tools and environments required for software development.
