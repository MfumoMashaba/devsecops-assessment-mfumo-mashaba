import sys
import argparse
from pathlib import Path

def secret_scan(repo_dir):
    print("----------BEGIN SCAN-------------")

# Recursively search for secrets
    try:
        from detect_secrets.core.scan import scan_file
        secrets_found = 0
        for path in Path(repo_dir).rglob('*'):
            if path.is_file():
                try:
                    secrets = scan_file(path)
                    for secret in secrets or []:
                        if secrets_found ==0:
                            print("Secret found")
                        print(f"in {path} {secret.type}  found on {secret.line_number} ") # if found display secret info
                        secrets_found += 1
                except Exception:
                    pass
        return secrets_found > 0
    except ImportError as e:
        print(f'{e} Install detect-secrets library')
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description='Secrets scanner')
    parser.add_argument('repo_dir', nargs='?', default='.', help='Your Workdir')
    if secret_scan(parser.parse_args().repo_dir):
        print('SECRETS FOUND')
        sys.exit(1)
    else:
        print("NO SECRETS FOUND")
        sys.exit(0)
if __name__ == '__main__':
    main()