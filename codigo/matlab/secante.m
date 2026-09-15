function [raiz, iter] = secante(f, x0, x1, tol, maxit)
% SECANTE  Metodo de la secante (Newton sin derivada). Chapra cap. 6.
%   Uso:  [r, n] = secante(@(x) x.^3 - x - 2, 1, 2, 1e-8, 50);
    for iter = 1:maxit
        f0 = f(x0); f1 = f(x1);
        x2 = x1 - f1*(x0 - x1)/(f0 - f1);
        if abs(x2 - x1) < tol, x1 = x2; break; end
        x0 = x1; x1 = x2;
    end
    raiz = x1;
end
