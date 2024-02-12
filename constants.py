
# MOVES
U = 'u'
U2 = 'u2'
U_PRIME = 'u_prime'

D = 'd'
D2 = 'd2'
D_PRIME = 'd_prime'

R = 'r'
R2 = 'r2'
R_PRIME = 'r_prime'

L = 'l'
L2 = 'l2'
L_PRIME = 'l_prime'

F = 'f'
F2 = 'f2'
F_PRIME = 'f_prime'

B = 'b'
B2 = 'b2'
B_PRIME = 'b_prime'

M = 'm'
M2 = 'm2'
M_PRIME = 'm_prime'

E = 'e'
E2 = 'e2'
E_PRIME = 'e_prime'

S = 's'
S2 = 's2'
S_PRIME = 's_prime'

X = 'x'
X2 = 'x2'
X_PRIME = 'x_prime'

Y = 'y'
Y2 = 'y2'
Y_PRIME = 'y_prime'

Z = 'z'
Z2 = 'z2'
Z_PRIME = 'z_prime'

# MOVES NEEDED TO SCRAMBLE CUBE
SCRAMBLE_MOVES = [
    U, U2, U_PRIME, D, D2, D_PRIME,
    R, R2, R_PRIME, L, L2, L_PRIME,
    F, F2, F_PRIME, B, B2, B_PRIME
]

CHECKER1 = {
    U: 1, U_PRIME: 1, U2: 1,
    D: 2, D_PRIME: 2, D2: 2,
    R: 3, R_PRIME: 3, R2: 3,
    L: 4, L_PRIME: 4, L2: 4,
    F: 5, F_PRIME: 5, F2: 5,
    B: 6, B_PRIME: 6, B2: 6,
}

CHECKER2 = {
    U: 1, U_PRIME: 1, U2: 1,
    D: 1, D_PRIME: 1, D2: 1,
    R: 2, R_PRIME: 2, R2: 2,
    L: 2, L_PRIME: 2, L2: 2,
    F: 3, F_PRIME: 3, F2: 3,
    B: 3, B_PRIME: 3, B2: 3,
}

NOT_U_AND_D = [R, R_PRIME, R2, L, L_PRIME, L2, F, F_PRIME, F2, B, B_PRIME, B2]
NOT_R_AND_L = [U, U_PRIME, U2, D, D_PRIME, D2, F, F_PRIME, F2, B, B_PRIME, B2]
NOT_F_AND_B = [U, U_PRIME, U2, D, D_PRIME, D2, R, R_PRIME, R2, L, L_PRIME, L2]

NOT_U_AND_D_AND_R_AND_L = [F, F_PRIME, F2, B, B_PRIME, B2]
NOT_R_AND_L_AND_F_AND_B = [U, U_PRIME, U2, D, D_PRIME, D2]
NOT_F_AND_B_AND_U_AND_D = [R, R_PRIME, R2, L, L_PRIME, L2]
