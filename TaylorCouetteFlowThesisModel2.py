# This file was generated by MathematicaToFEniCS
from MathematicaToFEniCS import *
from meshLine import *


# Problem constants



# initialization code
lam = Constant(0)
mus = Constant(10**-3)
mup = Constant(10**-2)
G = Constant(1)
H = Constant(10**-3)


# Define few useful expressions
ptxExpr = Expression(("x[0]","x[1]","x[2]"))
ptx = lambda i: ptxExpr[i]


# Initialize function spaces and functions
funSpaceLagrange2 = FunctionSpace(meshLine, 'Lagrange', 2)
totalSpace = MixedFunctionSpace([funSpaceLagrange2,funSpaceLagrange2,funSpaceLagrange2,funSpaceLagrange2,funSpaceLagrange2])
w = Function( totalSpace )
vt,Arr,Art,Att,Azz = split(w)
tvt,tArr,tArt,tAtt,tAzz = TestFunctions(totalSpace)


# Define weak form
def F1(w):
	vt,Arr,Art,Att,Azz = split(w)
	return (ptx(0)*Derivative(1)(tvt)*(mus*Derivative(1)(vt) + Art*(G - H*Derivative(2)(Arr)) - H*Att*Derivative(2)(Art)))*dx

def F2(w):
	vt,Arr,Art,Att,Azz = split(w)
	return ((ptx(0)*(2*Power(Art,2)*(-(G*tAzz) + G*Azz*tAzz + 2*H*tArt*Derivative(1)(Arr)*Derivative(1)(Art) + tArr*(-G + G*Arr + H*Power(Derivative(1)(Arr),2) + H*Power(Derivative(1)(Art),2)) + 2*H*tArt*Derivative(1)(Art)*Derivative(1)(Att) + tAtt*(-G + G*Att + H*Power(Derivative(1)(Art),2) + H*Power(Derivative(1)(Att),2)) + H*tAzz*Power(Derivative(1)(Azz),2) + H*Arr*Derivative(1)(Arr)*Derivative(1)(tArr) + H*Arr*Derivative(1)(Art)*Derivative(1)(tArt) + H*Att*Derivative(1)(Art)*Derivative(1)(tArt) + H*Att*Derivative(1)(Att)*Derivative(1)(tAtt) + H*Azz*Derivative(1)(Azz)*Derivative(1)(tAzz) - mup*Arr*tArt*Derivative(1)(vt) - mup*Att*tArt*Derivative(1)(vt)) + 2*Power(Art,3)*(2*G*tArt + H*Derivative(1)(Arr)*Derivative(1)(tArt) + H*Derivative(1)(Att)*Derivative(1)(tArt) + H*Derivative(1)(Art)*(Derivative(1)(tArr) + Derivative(1)(tAtt)) - mup*tArr*Derivative(1)(vt) - mup*tAtt*Derivative(1)(vt)) + Arr*(mup*Power(Arr,2)*tArt*Derivative(1)(vt) + Power(Att,2)*(-2*G*tAtt - 2*H*Derivative(1)(Art)*Derivative(1)(tArt) - 2*H*Derivative(1)(Att)*Derivative(1)(tAtt) + mup*tArt*Derivative(1)(vt)) - 2*Att*(-(G*tAzz) + G*Azz*tAzz + 2*H*tArt*Derivative(1)(Arr)*Derivative(1)(Art) + tArr*(-G + G*Arr + H*Power(Derivative(1)(Arr),2) + H*Power(Derivative(1)(Art),2)) + 2*H*tArt*Derivative(1)(Art)*Derivative(1)(Att) + tAtt*(-G + H*Power(Derivative(1)(Art),2) + H*Power(Derivative(1)(Att),2)) + H*tAzz*Power(Derivative(1)(Azz),2) + H*Arr*Derivative(1)(Arr)*Derivative(1)(tArr) + H*Arr*Derivative(1)(Art)*Derivative(1)(tArt) + H*Azz*Derivative(1)(Azz)*Derivative(1)(tAzz) - mup*Arr*tArt*Derivative(1)(vt))) - Arr*Art*(mup*Arr*(tArr - tAtt)*Derivative(1)(vt) + Att*(4*G*tArt + 2*H*Derivative(1)(Arr)*Derivative(1)(tArt) + 2*H*Derivative(1)(Att)*Derivative(1)(tArt) + 2*H*Derivative(1)(Art)*(Derivative(1)(tArr) + Derivative(1)(tAtt)) - mup*tArr*Derivative(1)(vt) - 3*mup*tAtt*Derivative(1)(vt)))))/(2.*(Power(Art,2) - Arr*Att)))*dx

FStatic = F1(w)+F2(w)


# Define boundary conditions
bc_vt_1 = DirichletBC(totalSpace.sub(0), 1, boundary_parts, 1)
bc_vt_2 = DirichletBC(totalSpace.sub(0), 0, boundary_parts, 2)
bc = [bc_vt_1,bc_vt_2]


# Initialize solver
JStatic = derivative(FStatic,w)
problemStatic = NonlinearVariationalProblem(FStatic,w,bc,JStatic)
solverStatic = NonlinearVariationalSolver(problemStatic)

prm = solverStatic.parameters
prm['newton_solver']['absolute_tolerance'] = 1E-8
prm['newton_solver']['relative_tolerance'] = 1E-7
prm['newton_solver']['maximum_iterations'] = 10
prm['newton_solver']['relaxation_parameter'] = 1.0


# post init code goes here
# Set initial conditions
ic = Expression(("0","1","0","1","1"))
w.assign(interpolate(ic,totalSpace))


# Solve
solverStatic.solve()

# Extra code
# post initialization code
vt,Arr,Art,Att,Azz = split(w)
plot( vt )
interactive()


