# Security Policy

## Supported Versions

We release patches for security vulnerabilities in the following versions:

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

The ConTextCap team takes security issues seriously. We appreciate your efforts to responsibly disclose your findings.

### How to Report a Security Vulnerability

**Please do not report security vulnerabilities through public GitHub issues.**

Instead, please report them using one of the following methods:

1. **GitHub Security Advisory** (Preferred)
   - Go to the [Security tab](https://github.com/awaliuddin/ConTextCap/security/advisories/new)
   - Click "Report a vulnerability"
   - Fill out the form with details

2. **Email**
   - Send an email to: [security@example.com]
   - Use "ConTextCap Security Issue" as the subject line
   - Include as much information as possible

### What to Include in Your Report

Please include the following information:

- Type of issue (e.g., buffer overflow, SQL injection, cross-site scripting, etc.)
- Full paths of source file(s) related to the manifestation of the issue
- The location of the affected source code (tag/branch/commit or direct URL)
- Any special configuration required to reproduce the issue
- Step-by-step instructions to reproduce the issue
- Proof-of-concept or exploit code (if possible)
- Impact of the issue, including how an attacker might exploit it

### What to Expect

After you submit a report:

1. **Acknowledgment**: We'll acknowledge receipt within 48 hours
2. **Assessment**: We'll assess the issue and determine its severity
3. **Communication**: We'll keep you updated on our progress
4. **Resolution**: We'll develop and test a fix
5. **Disclosure**: We'll coordinate disclosure with you
6. **Credit**: We'll give you credit for the discovery (unless you prefer to remain anonymous)

### Response Timeline

- **Initial Response**: Within 48 hours
- **Status Update**: Within 7 days
- **Fix Timeline**: Varies based on severity
  - Critical: Within 7 days
  - High: Within 30 days
  - Medium: Within 90 days
  - Low: Best effort

## Security Best Practices for Users

When using ConTextCap:

1. **Keep Updated**: Always use the latest version
2. **Review Files**: Be cautious when processing untrusted codebases
3. **Permissions**: Run with minimum necessary permissions
4. **Output**: Be careful where you save generated PDFs, especially with sensitive code
5. **Dependencies**: Keep Python and all dependencies updated

## Security Features

ConTextCap implements several security measures:

- **Input Validation**: All user inputs are validated
- **Path Sanitization**: File paths are sanitized to prevent directory traversal
- **Dependency Scanning**: Regular automated security scans of dependencies
- **Code Analysis**: Static code analysis with Bandit
- **Minimal Permissions**: Requests only necessary file system permissions

## Dependency Security

We monitor our dependencies for security vulnerabilities using:

- **Dependabot**: Automated dependency updates
- **Safety**: Python dependency vulnerability scanning
- **Bandit**: Security issue scanning in Python code

## Known Security Considerations

### File Access

ConTextCap requires read access to directories you select. It will:
- Only read files within the selected directory
- Not modify any source files
- Not transmit data over the network
- Not execute any code from processed files

### PDF Output

Generated PDFs contain:
- Source code from your project
- File structure information
- File metadata

**Important**: Do not share PDFs containing sensitive or proprietary code with untrusted parties.

## Security Updates

Security updates are released as soon as possible after a vulnerability is confirmed. Users will be notified through:

- GitHub Security Advisories
- Release notes
- GitHub Releases page

## Bug Bounty Program

We currently do not have a bug bounty program, but we deeply appreciate security researchers who help us keep ConTextCap secure.

## Disclosure Policy

We follow a **responsible disclosure** policy:

1. Security issues are fixed privately
2. Fixes are released as soon as possible
3. Public disclosure happens after fixes are available
4. Credit is given to researchers (with permission)

## Contact

For security concerns:
- **Security Email**: security@example.com
- **GitHub Security**: [Report a vulnerability](https://github.com/awaliuddin/ConTextCap/security/advisories/new)

For general questions:
- **GitHub Issues**: [Open an issue](https://github.com/awaliuddin/ConTextCap/issues)
- **Discussions**: [Start a discussion](https://github.com/awaliuddin/ConTextCap/discussions)

---

Thank you for helping keep ConTextCap and its users safe! 🔒
