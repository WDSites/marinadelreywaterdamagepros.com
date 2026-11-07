import importlib.util, os
PAGES = []
_d = os.path.dirname(os.path.abspath(__file__))
for _n in ('blog_a_1', 'blog_a_2', 'blog_a_3', 'blog_a_4'):
    _s = importlib.util.spec_from_file_location(_n, os.path.join(_d, _n + '.py'))
    _m = importlib.util.module_from_spec(_s); _s.loader.exec_module(_m)
    PAGES += _m.PAGES
