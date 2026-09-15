function x = gauss(A, b)
% GAUSS  Eliminacion gaussiana con pivoteo parcial. Chapra cap. 9.
%   Uso:  x = gauss([3 -0.1 -0.2; 0.1 7 -0.3; 0.3 -0.2 10], [7.85; -19.3; 71.4]);
    n = length(b);
    Ab = [A, b(:)];                          % matriz aumentada [A|b]
    for k = 1:n-1
        [~, p] = max(abs(Ab(k:n, k)));       % pivoteo parcial
        p = p + k - 1;
        if p ~= k, Ab([k p], :) = Ab([p k], :); end
        for i = k+1:n
            m = Ab(i,k)/Ab(k,k);
            Ab(i, k:end) = Ab(i, k:end) - m*Ab(k, k:end);
        end
    end
    x = zeros(n,1);                          % sustitucion hacia atras
    x(n) = Ab(n, end)/Ab(n, n);
    for i = n-1:-1:1
        x(i) = (Ab(i, end) - Ab(i, i+1:n)*x(i+1:n))/Ab(i, i);
    end
end
