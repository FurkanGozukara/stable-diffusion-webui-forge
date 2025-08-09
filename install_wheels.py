#!/usr/bin/env python
"""
Script to install wheel packages only if they're not already installed.
This prevents redownloading of large wheel files on every startup.
"""

import subprocess
import sys
import importlib.metadata
import platform

def is_package_installed(package_name):
    """Check if a package is installed."""
    try:
        importlib.metadata.version(package_name)
        return True
    except importlib.metadata.PackageNotFoundError:
        return False

def install_wheel_if_needed(package_name, wheel_url, platform_condition=None):
    """Install a wheel package only if not already installed."""
    
    # Check platform condition
    if platform_condition:
        current_platform = sys.platform
        if platform_condition == 'win32' and current_platform != 'win32':
            return
        elif platform_condition == 'linux' and not current_platform.startswith('linux'):
            return
    
    if is_package_installed(package_name):
        print(f"✓ {package_name} is already installed")
        return
    
    print(f"Installing {package_name} from {wheel_url}")
    subprocess.check_call([
        sys.executable, '-m', 'pip', 'install', 
        '--no-deps',  # Don't install dependencies (they're in requirements.txt)
        wheel_url
    ])

def main():
    """Install all wheel packages if needed."""
    
    wheels = [
        ('flash_attn', 
         'https://huggingface.co/MonsterMMORPG/SECourses_Premium_Flash_Attention/resolve/main/flash_attn-2.7.4.post1-cp310-cp310-win_amd64.whl',
         'win32'),
        ('flash_attn',
         'https://huggingface.co/MonsterMMORPG/SECourses_Premium_Flash_Attention/resolve/main/flash_attn-2.7.4.post1-cp310-cp310-linux_x86_64.whl',
         'linux'),
        ('xformers',
         'https://huggingface.co/MonsterMMORPG/SECourses_Premium_Flash_Attention/resolve/main/xformers-0.0.30+3abeaa9e.d20250424-cp310-cp310-win_amd64.whl',
         'win32'),
        ('xformers',
         'https://huggingface.co/MonsterMMORPG/SECourses_Premium_Flash_Attention/resolve/main/xformers-0.0.30+3abeaa9e.d20250427-cp310-cp310-linux_x86_64.whl',
         'linux'),
        ('sageattention',
         'https://github.com/woct0rdho/SageAttention/releases/download/v2.1.1-windows/sageattention-2.1.1+cu128torch2.7.0-cp310-cp310-win_amd64.whl',
         'win32'),
        ('sageattention',
         'https://huggingface.co/MonsterMMORPG/SECourses_Premium_Flash_Attention/resolve/main/sageattention-2.1.1-cp310-cp310-linux_x86_64.whl',
         'linux'),
    ]
    
    for package_name, wheel_url, platform_cond in wheels:
        install_wheel_if_needed(package_name, wheel_url, platform_cond)

if __name__ == '__main__':
    main()