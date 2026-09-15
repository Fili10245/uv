function yq = interp_lagrange(x, y, xq)
% INTERP_LAGRANGE  Interpolacion con polinomios de Lagrange. Chapra cap. 18.
%   Uso:  yq = interp_lagrange([1 2 4 5], [0 1 2 3], 3);
    n = numel(x); yq = zeros(size(xq));
    for i = 1:n
        Li = ones(size(xq));
        for j = 1:n
            if j ~= i
                Li = Li.*(xq - x(j))/(x(i) - x(j));
            end
        end
        yq = yq + y(i)*Li;
    end
end
