#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: regi

Foi usado assim:
t000xml(range(1,3),range(-2,3),range(-2,3))

"""

import math
import sympy as sy
from sympy import I
    

def t000xml(aa,bb,cc):
    

# lê um arquivo que foi exportado do Moodle com uma questão teste depois de ser editado para a retirada da questão 
#    e da última linha que contem </quiz>
    contents = open("Equacoes-do-2o-grau.xml").read()
# cria o arquivo onde as questões serão escritas 
    open("t-0-0-0.xml", "w").write(contents)

    
    fid= open('t-0-0-0.xml','a')
    x = sy.Symbol('x')
    nq=0
    for a in aa:
        for b in bb:
            for c in cc:
                    if (a>0)and(abs(b)+abs(c)>0):
                        if (math.gcd(math.gcd(a,b),c)==1):
                            nq=nq+1
                            Delta=b**2-4*a*c
                            fid.write('<question type="multichoice">\n')
                            fid.write('    <name>\n')
                            fid.write('      <text>[0.0][0]a='+str(a)+',b='+str(b)+',c='+str(c)+',Delta='+str(Delta)+'</text>\n')
                            fid.write('    </name>\n')
                            fid.write('    <questiontext format="html">\n')
                            fid.write('      <text><![CDATA[ ')
                            fid.write('<p>Determine a(s) solução(ões) da equação</p>\n')
                            fid.write('<p>\\[  \n')
                            fid.write(' '+sy.latex(a*x**2 + b*x +c)+'=0. \n')
                            fid.write('\\]</p> \n')
                            fid.write(']]></text>\n    </questiontext>\n ')
            #
                            fid.write('    <generalfeedback format="html"> \n')
                            fid.write('      <text><![CDATA[ ')
                            fid.write('<p>Esta é uma equação de 2<sup>o</sup> grau da forma \\(ax^2+bx+c=0\\), com \\(a='+str(a)+'\\), \\(b='+str(b)+'\\) e \\(c='+str(c)+'\\).</p> \n')
                            fid.write('<p>\\[ \n')
                            fid.write('\\Delta=b^2-4ac='+str(Delta)+'. \n ')
                            fid.write('\\]</p> \n')
                            if (Delta>0):
                                fid.write('<p>Como \\(\\Delta > 0\\), esta equação tem duas raizes reais:</p>\n')
                                fid.write('<p>\\[ \n')
                                fid.write('x_{1,2}=\\frac{-b\\pm\\sqrt{\\Delta}}{2a}.\n ')
                                fid.write('\\]</p> \n')
                                fid.write('<p>Ou seja,</p>\n')
                                fid.write('<p>\\[ \n')
                                fid.write('x_1='+sy.latex(sy.sympify(sy.Rational(-b,2*a)-sy.sqrt(Delta)/(2*a)))+'\\text{ e }x_2='+sy.latex(sy.sympify(sy.Rational(-b,2*a)+sy.sqrt(Delta)/(2*a)))+'.\n ')
                                fid.write('\\]</p> \n')
                            if (Delta<0):
                                fid.write('<p>Como \\(\\Delta < 0\\), esta equação tem duas raizes complexas:</p>\n')
                                fid.write('<p>\\[ \n')
                                fid.write('x_{1,2}=\\frac{-b\\pm\\sqrt{-\\Delta}\\, i}{2a}.\n ')
                                fid.write('\\]</p> \n')
                                fid.write('<p>Ou seja,</p>\n')
                                fid.write('<p>\\[ \n')
                                fid.write('x_1='+sy.latex(sy.sympify(sy.Rational(-b,2*a)-sy.sqrt(-Delta)/(2*a)*I))+'\\text{ e }x_2='+sy.latex(sy.sympify(sy.Rational(-b,2*a)+sy.sqrt(-Delta)/(2*a)*I))+'.\n ')
                                fid.write('\\]</p> \n')
                            if (Delta==0):
                                fid.write('Como \\(\\Delta = 0\\), esta equação tem somente uma raiz real:\n')
                                fid.write('<p>\\[ \n')
                                fid.write('x=-\\frac{b}{2a}='+sy.latex(sy.sympify(sy.Rational(-b,2*a)))+'.\n ')
                                fid.write('\\]</p> \n')
                            fid.write(']]></text> \n ')
                            fid.write('    </generalfeedback> \n')
                #            #
                            fid.write(' <defaultgrade>1.0000000</defaultgrade>\n <penalty>0.3333333</penalty>\n <hidden>0</hidden>\n <idnumber></idnumber>\n')
                            fid.write(' <single>true</single>\n <shuffleanswers>true</shuffleanswers>\n <answernumbering>abc</answernumbering>\n <correctfeedback format="html">\n')
                            fid.write(' <text>Sua resposta está correta.</text>\n </correctfeedback>\n <partiallycorrectfeedback format="html">\n ')
                            fid.write(' <text>Sua resposta está parcialmente correta.</text>\n </partiallycorrectfeedback>\n <incorrectfeedback format="html">\n ')
                            fid.write(' <text>Sua resposta está incorreta.</text>\n </incorrectfeedback>\n <shownumcorrect/>\n ')
                #            #
                            fid.write('    <answer fraction="100" format="html"> \n')#a
                            fid.write('      <text><![CDATA[ ')
                            if (Delta>0):
                                fid.write('<p>\\(x_1='+sy.latex(sy.sympify(sy.Rational(-b,2*a)-sy.sqrt(Delta)/(2*a)))+'\\text{ e }x_2='+sy.latex(sy.sympify(sy.Rational(-b,2*a)+sy.sqrt(Delta)/(2*a)))+' \\)</p>\n')
                            elif(Delta<0):
                                fid.write('<p>x\\(_1='+sy.latex(sy.sympify(sy.Rational(-b,2*a)-sy.sqrt(-Delta)/(2*a)*I))+'\\text{ e }x_2='+sy.latex(sy.sympify(sy.Rational(-b,2*a)+sy.sqrt(-Delta)/(2*a)*I))+'\\) </p>\n')
                            elif (Delta==0):
                                fid.write('<p>\\(x='+sy.latex(sy.sympify(sy.Rational(-b,2*a)))+'\\) </p>\n')
                            fid.write(']]></text> \n ')
                            fid.write('      <feedback format="html">\n <text></text>\n </feedback>\n </answer>\n ')
                            fid.write('    <answer fraction="0" format="html"> \n')#b
                            fid.write('      <text><![CDATA[ ')
                            if (Delta>0):
                                fid.write('<p>\\(x_1='+sy.latex(sy.sympify(sy.Rational(b,2*a)-sy.sqrt(Delta)/(2*a)))+'\\text{ e }x_2='+sy.latex(sy.sympify(sy.Rational(b,2*a)+sy.sqrt(Delta)/(2*a)))+' \\)</p>\n')
                            elif(Delta<0):
                                fid.write('<p>\\(x_1='+sy.latex(sy.sympify(sy.Rational(b,2*a)-sy.sqrt(-Delta)/(2*a)*I))+'\\text{ e }x_2='+sy.latex(sy.sympify(sy.Rational(b,2*a)+sy.sqrt(-Delta)/(2*a)*I))+'\\) </p>\n')
                            elif (Delta==0):
                                fid.write('<p>\\(x='+sy.latex(sy.sympify(sy.Rational(b,2*a)))+'\\) </p>')
                            fid.write(']]></text> \n ')
                            fid.write('      <feedback format="html">\n <text></text>\n </feedback>\n </answer>\n ')
                            fid.write('    <answer fraction="0" format="html"> \n')#c
                            fid.write('      <text><![CDATA[ ')
                            if (Delta>0):
                                fid.write('<p>\\(x_1='+sy.latex(sy.sympify(sy.Rational(-b,a)-sy.sqrt(Delta)/(a)))+'\\text{ e }x_2='+sy.latex(sy.sympify(sy.Rational(-b,a)+sy.sqrt(Delta)/(a)))+' \\)</p>\n')
                            elif(Delta<0):
                                fid.write('<p>\\(x_1='+sy.latex(sy.sympify(sy.Rational(-b,a)-sy.sqrt(-Delta)/(a)*I))+'\\text{ e }x_2='+sy.latex(sy.sympify(sy.Rational(-b,a)+sy.sqrt(-Delta)/(a)*I))+'\\) </p>\n')
                            elif (Delta==0):
                                fid.write('<p>\\(x='+sy.latex(sy.sympify(sy.Rational(-b,a)))+'\\) </p>\n')
                            fid.write(']]></text> \n ')
                            fid.write('      <feedback format="html">\n <text></text>\n </feedback>\n </answer>\n ')
                            fid.write('    <answer fraction="0" format="html"> \n')#d
                            fid.write('      <text><![CDATA[ ')
                            if (Delta>0):
                                fid.write('<p>\\(x_1='+sy.latex(sy.sympify(sy.Rational(-b,2*a)-sy.sqrt(Delta)/(2*a)*I))+'\\text{ e }x_2='+sy.latex(sy.sympify(sy.Rational(-b,2*a)+sy.sqrt(Delta)/(2*a)*I))+' \\)</p>\n')
                            elif(Delta<0):
                                fid.write('<p>\\(x_1='+sy.latex(sy.sympify(sy.Rational(-b,2*a)-sy.sqrt(-Delta)/(2*a)))+'\\text{ e }x_2='+sy.latex(sy.sympify(sy.Rational(-b,2*a)+sy.sqrt(-Delta)/(2*a)))+'\\) </p>\n')
                            elif (Delta==0):
                                fid.write('<p>\\(x_1='+sy.latex(sy.sympify(sy.Rational(-b,2*a)))+'\\text{ e }x_2='+sy.latex(sy.sympify(sy.Rational(b,2*a)))+'\\) </p>')
                            fid.write(']]></text> \n ')
                            fid.write('      <feedback format="html">\n <text></text>\n </feedback>\n </answer>\n ')
                            fid.write('    <answer fraction="0" format="html"> \n')#e
                            fid.write('      <text><![CDATA[ ')
                            if (Delta>0):
                                fid.write('<p>\\(x='+sy.latex(sy.sympify(sy.Rational(-b,2*a)-sy.sqrt(Delta)/(2*a)))+'\\)</p>\n')
                            elif(Delta<0):
                                fid.write('<p>\\(x='+sy.latex(sy.sympify(sy.Rational(-b,2*a)-sy.sqrt(-Delta)/(2*a)))+'\\) </p>\n')
                            elif (Delta==0):
                                fid.write('<p>\\(x_1='+sy.latex(sy.sympify(sy.Rational(-b,a)))+'\\text{ e }x_2='+sy.latex(sy.sympify(sy.Rational(b,a)))+'\\) </p>')
                            fid.write(']]></text> \n ')
                            fid.write('      <feedback format="html">\n <text></text>\n </feedback>\n </answer>\n ')
                            fid.write('  </question>\n\n')
    print('Total: '+str(nq)+' questões')
    fid.write('</quiz>\n\n')
    fid.close()
    
