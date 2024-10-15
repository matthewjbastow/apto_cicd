import os
import tarfile
import sys

def package_splunk_app(app_dir, output_file):
    with tarfile.open(output_file, "w:gz") as tar:
        tar.add(app_dir, arcname=os.path.basename(app_dir))
    print(f"Packaged {app_dir} into {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python package_splunk_app.py <app_dir> <output_file>")
        sys.exit(1)

    app_dir = sys.argv[1]
    output_file = sys.argv[2]
    package_splunk_app(app_dir, output_file)