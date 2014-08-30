def euler_maclaurin_quad(start,end,n_points):
    roots = [start + i*float(end - start)/n_points for i in range(0,n_points+1)]
    weights = [(end-start)*float(1)/n_points]*n_points
    weights[0] = weights[0]/2
    weights[-1] = weights[-1]/2
    return weights,roots
# We use our own because numpy doesnt get within 1e-14 for 7th order poly, unsure why
# Credit for roots/weights: http://pomax.github.io/bezierinfo/legendre-gauss.html
def gauss_legendre_quad(n_points):
    if n_points == 2:
        weights = [1.0,1.0]
        roots = [-0.5773502691896257,0.5773502691896257]
    elif n_points == 3:
        weights = [0.8888888888888888,0.5555555555555556,0.5555555555555556]
        roots = [0.0000000000000000,-0.7745966692414834,0.7745966692414834]
    elif n_points == 4:
        weights = [0.6521451548625461,0.65214515486254610,0.3478548451374538,0.3478548451374538]
        roots = [-0.3399810435848563,0.3399810435848563,-0.8611363115940526,0.8611363115940526]
    elif n_points == 5:
        weights = [0.5688888888888889,0.4786286704993665,0.4786286704993665,0.2369268850561891,0.2369268850561891]
        roots = [0.0000000000000000,-0.5384693101056831,0.5384693101056831,-0.9061798459386640,0.9061798459386640]
    elif n_points == 6:
        weights = [0.3607615730481386,0.3607615730481386,0.4679139345726910,0.4679139345726910,0.1713244923791704,0.1713244923791704]
        roots = [0.6612093864662645,-0.6612093864662645,-0.2386191860831969,0.2386191860831969,-0.9324695142031521,0.9324695142031521]
    elif n_points == 7:
        weights = [0.4179591836734694,0.3818300505051189,0.3818300505051189,0.2797053914892766,0.2797053914892766,0.1294849661688697,0.1294849661688697]
        roots = [0.0000000000000000,0.4058451513773972,-0.4058451513773972,-0.7415311855993945,0.7415311855993945,-0.9491079123427585,0.9491079123427585]
    elif n_points == 8:
        weights = [0.3626837833783620,0.3626837833783620,0.3137066458778873,0.3137066458778873,0.2223810344533745,0.2223810344533745,0.1012285362903763,0.1012285362903763]
        roots = [-0.1834346424956498,0.1834346424956498,-0.5255324099163290,0.5255324099163290,-0.7966664774136267,0.7966664774136267,-0.9602898564975363,0.9602898564975363]
    elif n_points == 9:
        weights = [0.3302393550012598,0.1806481606948574,0.1806481606948574,0.0812743883615744,0.0812743883615744,0.3123470770400029,0.3123470770400029,0.2606106964029354,0.2606106964029354]
        roots = [0.0000000000000000,-0.8360311073266358,0.8360311073266358,-0.9681602395076261,0.9681602395076261,-0.3242534234038089,0.3242534234038089,-0.6133714327005904,0.6133714327005904]
    else:
        raise ValueError("Unsupported number of points")
    return weights,roots