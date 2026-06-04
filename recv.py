
import base64, os, sys
chunk = sys.stdin.read().strip()
mode = sys.argv[1] if len(sys.argv) > 1 else 'a'
path = os.path.expanduser('~/sns-design-system/.b64chunks')
with open(path, mode) as f:
    f.write(chunk)
print(f"Wrote {len(chunk)} chars, mode={mode}")
