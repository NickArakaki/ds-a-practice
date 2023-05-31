def sockMerchant(n, ar):
    seen_socks = set()
    num_pairs = 0

    for sock in ar:
        if sock in seen_socks:
            num_pairs += 1
            seen_socks.remove(sock)
        else:
            seen_socks.add(sock)

    return num_pairs

print(sockMerchant(9, [10,20,20,10,10,30,50,10,20])) # 3
