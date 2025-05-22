# Ansible Role: systemd_service

[![CI](https://github.com/1000Bulbs/ansible-role-systemd_service/actions/workflows/ci.yml/badge.svg)](https://github.com/1000Bulbs/ansible-role-systemd_service/actions/workflows/ci.yml)

Manages the state of systemd services on Linux systems. It provides a flexible interface for starting, stopping, enabling, disabling, reloading, and restarting services using the `systemd` module. The role is ideal for infrastructure automation where consistent and repeatable service management is required.

---

## ✅ Requirements

- Ansible 2.13+
- Python 3.9+ (for Molecule + testinfra)
- Tested on Ubuntu 22.04+

---

## ⚙️ Role Variables

These variables can be overridden in your inventory, playbooks, or `group_vars`.

### Defaults (`defaults/main.yml`)

| Variable                  | Description                                                                           | Default Value |
| ------------------------- | ------------------------------------------------------------------------------------- | ------------- |
| `systemd_service_name`    | **Required.** The name of the systemd service to manage.                              | —             |
| `systemd_service_enabled` | Whether the service should be enabled at boot.                                        | `false`       |
| `systemd_service_state`   | Desired state of the service. Options: `started`, `stopped`, `restarted`, `reloaded`. | `started`     |

### Variables (`vars/main.yml`)

_No variables defined._

---

## 📦 Dependencies

_None._

---

## 📥 Installing the Role

To include this role in your project using a `requirements.yml` file:

```yaml
roles:
  - name: okb.systemd_service
    src: https://github.com/1000bulbs/ansible-role-systemd_service.git
    scm: git
    version: master
```

Then install it with:

```bash
ansible-galaxy role install -r requirements.yml
```

---

## 💡 Example Playbook

```yaml
- name: Manage example systemd service
  hosts: all
  become: true
  roles:
    - role: okb.systemd_service
      vars:
        systemd_service_name: example
        systemd_service_enabled: true
        systemd_service_state: started
```

---

## 🧪 Testing

This role uses Python and Node.js for linting and formatting, Molecule with pytest-testinfra for integration testing,
and Act for local GitHub Actions testing — all orchestrated through a Makefile for ease of use and convenience.

### Install dependencies

Install all dependencies and setup environment

```bash
make setup
```

### Run tests locally

#### Lint and Format Checks

Run lint and format checks

```bash
make check
```

#### Integration Tests

Run integration tests

```bash
make test
```

#### GitHub Actions Tests

Run github actions tests locally

```bash
make ci
```

---

## 🪝 Git Hooks

This project includes [pre-commit](https://pre-commit.com/) integration via Git hooks to automatically run formatting and linting checks **before each commit**.

These hooks help catch errors early and keep the codebase consistent across contributors.

### Prerequisites

Before installing the hooks, make sure your system has:

- **Python 3.9+** with `pip` installed
- **Node.js** and `npm` (required for `markdownlint-cli2`)

You can check your versions with:

```bash
python3 --version
pip --version
node --version
npm --version
```

### Install Git Hooks

```bash
make install-hooks
```

This will:

- Install pre-commit (if not already installed)
- Register a Git hook in .git/hooks/pre-commit
- Automatically run checks like:
- Code formatting with black and isort
- Linting with ruff, yamllint, and ansible-lint

### Test Git Hooks

```bash
make test-hooks
```

This will run the pre-commit hooks on all files, the same as when you run `git commit`.

### Remove Git Hooks

```bash
make uninstall-hooks
```

This removes the Git pre-commit hook and disables automatic checks.

💡 Even with hooks uninstalled, you can still run the same checks manually with `make test-hooks`.

Why Use Git Hooks?

- Ensures consistency across contributors
- Catches syntax and style issues before they hit CI
- Prevents accidental commits of broken or misformatted files
- Integrates seamlessly with your local workflow
