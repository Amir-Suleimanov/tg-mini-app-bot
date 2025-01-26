#!/usr/bin/env python
import sys
import os

# Добавляем путь к папке backend
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError("Couldn't import Django.") from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()