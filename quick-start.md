# 🦔 Hedgehog Showcase — Quick Start

## Download

```bash
git clone https://github.com/Y42-gladiolus/hedgehog-showcase.git
cd hedgehog-showcase
Run
# Run all implementations
./run.sh

# Or run individual
./bin/hedgehog-ocaml
./bin/hedgehog-rust
./bin/hedgehog-ada
./bin/hedgehog-nim
./bin/hedgehog-zig
Expected Output
All should output:
Serialized: 113 bytes
CRC32: xxxxxxxx
Configure
Edit rules.json:
{
  "consensus_threshold": 0.75,
  "actions": {
    "alert": { "severity": "critical" }
  }
}
View Dashboard
Open index.html in browser:
# Linux
xdg-open index.html

# macOS
open index.html

# Windows
start index.html
What This Shows
5 independent implementations
All produce identical 113-byte frames
Byzantine fault tolerance in action
No single point of failure
For Clients
This demonstrates my ability to build:
Verification systems
Multi-language implementations
Fault-tolerant architectures
Compliance-ready solutions
Contact: [Your email/Telegram]
