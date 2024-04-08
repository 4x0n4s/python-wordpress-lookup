import requests
import sys
import os

class WordPress:
    def __init__(
        self,
        host: str = None,
    ) -> None:
        self.host = host
        self.results = []
        self.wordpress_endpoints = [
            'wp-admin/impages', 'wp-admin-includes', 'wp-admin/js', 'wp-amin/maint',
            'wp-admin/network', 'wp-admin/admin/users', 'wp-content/uploads',
            'wp-includes/js', 'wp-includes/js/tinymce/puglins', 'wp-includes/theme-compat',
            'wp-config.php'
        ]
        self.wordpress_identifiers = ['wordpress', 'wp-content', 'wp-includes']

    def is_wordpress(self, url: str) -> bool:
        try:
            req = requests.get(url)
            if req.status_code == 200:
                return bool(identifier in req.text for identifier in self.wordpress_identifiers)
            return False
        except requests.RequestException:
            return False

    def lookup(self) -> None:
        if self.is_wordpress(self.host):
            try:
                print(f'{self.host} is a WordPress site.')
                for file in self.wordpress_endpoints:
                    url = f'{self.host}/{file}'
                    req = requests.get(url)
                    if req.status_code == 200:
                        self.results.append(url)
                if self.results:
                    print(self.results)
                else:
                    print('0 endpoints')
                
            except:
                print(f'{self.host} is not a WordPress site or could not be reached.')
                sys.exit(1)
        else:
            print(f'{self.host} is not a WordPress site or could not be reached.')
            sys.exit(1)