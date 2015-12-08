{% for pkg in 'git', 'nginx', 'python-dev', 'python-virtualenv', 'supervisor' %}
pkg_{{ pkg }}:
  pkg.installed:
    - name: {{ pkg }}
{% endfor %}

git_fibonappi:
  git.latest:
    - name: git@github.com:jessegonzalez/fibonappi.git
    - rev: master
    - target: /opt/fibonappi
    - require:
      - pkg: pkg_git

virtualenv_/opt/fibonappi/venv:
  virtualenv.managed:
    - requirements: /opt/fibonappi/requirements.txt
    - require:
      - git_fibonappi

file_/var/run/fibonappi:
  file.directory:
    - name: /var/run/fibonappi
    - mode: 0777
    - user: www-data
    - group: www-data

file_/var/log/fibonappi:
  file.directory:
    - name: /var/log/fibonappi
    - user: www-data
    - group www-data

file_/etc/supervisor/conf.d/fibonappi.conf:
  file.managed:
    - name: /etc/supervisor/conf.d/fibonappi.conf
    - source: /opt/fibonappi/fibonappi.conf
    - require:
      - pkg: pkg_supervisor
      - git: git_fibonappi
    - watch_in:
      - service: service_supervisor

file_/etc/nginx/sites-enabled/default:
  file.absent
    - name: /etc/nginx/sites-enabled/default

file_/etc/nginx/sites-available/fibonappi:
  file.managed:
    - name: /etc/nginx/sites-avilable/fibonappi
    - source: /opt/fibonappi/fibonappi-nginx
    - require:
      - pkg: pkg_nginx
      - git: git_fibonappi
    - watch_in:
      - service: service_nginx

service_nginx:
  service.running:
    - name: nginx
    - require:
      - file: file_/etc/nginx/sites-available/fibonappi

service_supervisor:
  service.running:
    - name: supervisor
    - require:
      - file: file_/etc/supervisor/conf.d/fibonappi.conf
