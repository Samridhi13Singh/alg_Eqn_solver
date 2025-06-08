import streamlit as st
import numpy as np
from scipy.linalg import solve
from scipy.odr import quadratic

st.set_page_config(page_title="Algebraic eqn solver",layout="wide")
st.title("Algebraic Eqn Solver")
st.markdown("Solve linear, quadratic, cubic and system of eqn")
linear= "linear (ax+b=0)"
quadratic="quadratic(ax² + bx + c = 0))"
cubic="cubic(ax³ + bx² + cx + d = 0)"
options = st.sidebar.radio(
    "Choose a type of eqn to solve:-",
    (linear,quadratic,cubic,"system of two eqns","system of 3 eqns")
)
st.divider()

if options==linear:
    st.subheader("Linear eqn")
    a=st.number_input("enter a coefficient",value=1)
    b=st.number_input("enter a constant",value=1)
    st.latex(fr"{a}x + {b}")
    if st.button("Solve Linear Eqn"):
        if a!=0:
          result=-b/a
          st.success(f"The root is {result}")
        else:
            st.error("NOT A VALID LINEAR EQN")


elif options==quadratic:
    st.subheader("Quadratic eqn")
    a=st.number_input("enter a coefficient a:", value=1)
    b=st.number_input("enter a coefficient b:",value=1)
    c=st.number_input("enter a constant",value=1)
    st.latex(fr"{a}x^2 + {b}x + {c}")
    if st.button("Solve Quadratic Eqn"):
        coeff=[a,b,c]
        roots=np.roots(coeff)
        st.success(f"the roots are {roots[0]} and {roots[1]}")


elif options==cubic:
    st.subheader("Cubic eqn")
    a=st.number_input("Enter a coefficient a:",value=1)
    b=st.number_input("Enter a coefficient b:",value=1)
    c=st.number_input("Enter a coefficient c",value=1)
    d=st.number_input("Enter a constant ",value=1)
    st.latex(fr"{a}x^3 +{b}x^2 +{c}x +{d}")
    if st.button("Solve Cubic Eqn"):
        coef=[a,b,c,d]
        root=np.roots(coef)
        st.success(f"The roots are{root[0]} , {root[1]} and {root[2]}")

elif options=="system of two eqns":
    st.subheader("system of two eqns")
    x1=st.number_input("Enter the coeff of x(eqn1):",value=1)
    y1=st.number_input("Enter the coeff of y(eqn1):",value=1)
    x2 = st.number_input("Enter the coeff of x(eqn2):", value=1)
    y2 = st.number_input("Enter the coeff of y(eqn2):", value=1)
    c1=st.number_input("Enter a constant of c(eqn1):",value=1)
    c2 = st.number_input("Enter a constant of c(eqn2):", value=1)
    st.latex(fr"({x1})x + ({y1})y = {c1}")
    st.latex(fr"({x2})x + ({y2})y = {c2}")
    if st.button("Solve the 2 Eqns"):
        coeff=np.array([
            [x1,y1],
            [x2,y2]
        ])
        cons=np.array([c1,c2])
        val=solve(coeff,cons)
        st.success(f"the value of x(s) {val[0]} and value of y {val[1]}")

elif options=="system of 3 eqns":
    st.subheader("system of 3 eqns")
    x1=st.number_input("Enter the coeff of x(eqn1):",value=1)
    y1=st.number_input("Enter the coeff of y(eqn1):",value=1)
    z1=st.number_input("Enter the coeff of z(eqn1):",value=1)

    x2=st.number_input("Enter the coeff of x(eqn2):", value=1)
    y2 = st.number_input("Enter the coeff of y(eqn2):", value=1)
    z2 = st.number_input("Enter the coeff of z(eqn2):", value=1)

    x3 = st.number_input("Enter the coeff of x(eqn3):", value=1)
    y3 = st.number_input("Enter the coeff of y(eqn3):", value=1)
    z3 = st.number_input("Enter the coeff of z(eqn3):", value=1)

    c1=st.number_input("Enter a constant of c(eqn1):",value=1)
    c2=st.number_input("Enter a constant of c(eqn2):",value=1)
    c3=st.number_input("Enter a constant of c(eqn3):",value=1)
    st.latex(fr"({x1})x + ({y1})y  + ({z1})z= {c1}")
    st.latex(fr"({x2})x + ({y2})y + ({z2})z= {c2}")
    st.latex(fr"({x3})x + ({y3})y + ({z3})z= {c3}")

    if st.button("Solve for 3 Eqn"):
        coeff = np.array([
            [x1, y1,z1],
            [x2, y2,z2],
            [x3,y3,z3]
        ])
        cons = np.array([c1, c2,c3])
        val = solve(coeff, cons)
        st.success(f"The value of x {val[0]} \n The  value of y {val[1]} \n The value for z{val[2]}")
