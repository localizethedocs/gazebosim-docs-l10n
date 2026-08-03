import sys
from pathlib import Path
import yaml
from build_multiversion import generate_sources

def main():
    src_dir = Path(".")  # points to your project directory
    tmp_dir = src_dir / ".tmp"
    tmp_dir.mkdir(exist_ok=True)

    # read index.yaml
    with open(src_dir / "index.yaml") as f:
        gz_nav_yaml = yaml.safe_load(f)

    # extract command line argument as release
    if len(sys.argv) < 2:
        print("Usage: python generate_sources.py <release>")
        sys.exit(1)

    release = sys.argv[1]
    generate_sources(gz_nav_yaml, src_dir, tmp_dir, release)

if __name__ == "__main__":
    main()
