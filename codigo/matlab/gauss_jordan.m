function [x, Inv] = gauss_jordan(A, b)
% GAUSS_JORDAN  Gauss-Jordan con pivoteo: solucion e inversa. Chapra cap. 9-10.
%   Uso:  [x, Inv] = gauss_jordan([3 -0.1 -0.2; 0.1 7 -0.3; 0.3 -0.2 10], ...
%                                 [7.85; -19.3; 71.4]);
    n = size(A,1);
    M = [A, eye(n), b(:)];                    % [A | I | b]
    for k = 1:n
        [~, p] = max(abs(M(k:n, k))); p = p + k - 1;
        if p ~= k, M([k p], :) = M([p k], :); end
        M(k, :) = M(k, :)/M(k, k);            % normaliza el pivote
        for i = 1:n
            if i ~= k
                M(i, :) = M(i, :) - M(i, k)*M(k, :);
            end
        end
    end
    Inv = M(:, n+1:2*n);
    x   = M(:, end);
end
