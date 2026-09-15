function yq = interp_newton(x, y, xq)
% INTERP_NEWTON  Interpolacion por diferencias divididas de Newton. Chapra cap. 18.
%   Uso:  yq = interp_newton([1 2 4 5], [0 1 2 3], 3);
    n = numel(x); c = y(:);
    for j = 2:n                               % diferencias divididas
        for i = n:-1:j
            c(i) = (c(i) - c(i-1))/(x(i) - x(i-j+1));
        end
    end
    yq = c(n)*ones(size(xq));                 % evaluacion (Horner anidado)
    for k = n-1:-1:1
        yq = yq.*(xq - x(k)) + c(k);
    end
end
