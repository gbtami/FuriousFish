import requests

class Fishtest():
    pass


def get_test_info(msg):
    """Extract test info from commit message

    First look for text between {...} parenthesis after the @submit marker, if
    not found fallback on the commit title.

    We assume the message has always a @submit marker.
    """
    s = msg.split('\n@submit', 1)
    info = [p.split('}')[0] for p in s[1].split('{') if '}' in p and s[1] != p]
    if not info:
        info = [p for p in s[0].splitlines() if p]
        if not info:
            return None
    return info[0].strip()


def forge_post():
    """
    http://tests.stockfishchess.org/tests/run

    import requests
    headers = {'User-Agent': 'Mozilla/5.0'}
    payload = {'username':'niceusername','password':'123456'}

    session = requests.Session()
    session.post('https://admin.example.com/login.php',headers=headers,data=payload)
    # the session instance holds the cookie. So use it to get/post later.
    # e.g. session.get('https://example.com/profile')


    http://wwwsearch.sourceforge.net/mechanize/

     url='http://tests.stockfishchess.org/tests/run'
     user='mcostalba'
     pwd='xxxxxx'

 import mechanize

 br = mechanize.Browser()
 br.set_handle_robots(False)
 br.addheaders = [("User-agent","Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.13) Gecko/20101206 Ubuntu/10.10 (maverick) Firefox/3.6.13")]
 sign_in=br.open(url)
 br.select_form(nr = 0)
 br["username"] = user
 br["password"] = pwd
 logged_in = br.submit()
 logincheck = logged_in.read()


    """
    map = {
            'sha'        : 'test-branch',
            'bench_head' : 'test-signature',
            'bench_base' : 'base-signature',
            'repo_url'   : 'tests-repo',
            'test_info'   : 'run-info' } # FIXME ! MISSING

    payload = { 'test_type': 'Standard',
                'test-branch': 'HEAD',
                'new-options' :'Hash=128',
                'test-signature' : '77777',
                'base-branch' : 'master',
                'base-options' : 'Hash=128',
                'base-signature' : '888888',
                'stop_rule' : 'sprt',
                'num-games' : '20000',
                'sprt_elo0' : '0',
                'sprt_elo1' : '5',
                'spsa_A' : '5000',
                'spsa_gamma' : '0.101',
                'spsa_alpha' : '0.602',
                'spsa_raw_params' : 'Aggressiveness,30,0,200,10,0.0020',
                'tc' : '15+0.05',
                'threads' : '1',
                'book' : '2moves_v1.pgn',
                'book-depth' : '8',
                'priority': '0',
                'throughput': '1000',
                'tests-repo' : 'https://github.com/username/Stockfish',
                'run-info' : 'test note field' }
    pass