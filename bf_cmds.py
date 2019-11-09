def forward(fixed, mem, i, ip, output, brackets):
    if not fixed and i + 1 >= len(mem):
        mem.extend([0 for _ in range(1000)])
    return i + 1, ip + 1

def backward(fixed, mem, i, ip, output, brackets):
    return i - 1, ip + 1

def inc(fixed, mem, i, ip, output, brackets):
    mem[i] += 1
    return i, ip + 1

def dec(fixed, mem, i, ip, output, brackets):
    mem[i] -= 1
    return i, ip + 1

def out(fixed, mem, i, ip, output, brackets):
    output.append(chr(mem[i]))
    return i, ip + 1

def inp(fixed, mem, i, ip, output, brackets):
    print(''.join(output), end='')
    del output[:]

    mem[i] = ord(input('\n')[0])
    return i, ip + 1

def loop_start(fixed, mem, i, ip, output, brackets):
    if mem[i] == 0:
        return i, brackets[ip + 1]
    
    return i, ip + 1

def loop_end(fixed, mem, i, ip, output, brackets):
    if mem[i] != 0:
        return i, brackets[ip + 1]
    
    return i, ip + 1