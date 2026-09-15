% error_relativo.m -- Errores absoluto, relativo y aproximado. Chapra cap. 3.
% Script con funcion local (requiere R2016b+ / Octave).

[ea, er] = errores(pi, 22/7);
fprintf('Aproximacion 22/7 de pi:\n');
fprintf('  Error absoluto = %.6e\n', ea);
fprintf('  Error relativo = %.6e (%.4f%%)\n', er, er*100);

% Criterio de paro por error relativo aproximado entre iteraciones
tol = 1e-4; x_prev = 1; x_curr = 1.5; k = 0;
while true
    k = k + 1;
    erp = abs((x_curr - x_prev)/x_curr);      % error relativo aproximado
    if erp < tol, break; end
    x_prev = x_curr;
    x_curr = 0.5*(x_curr + 2/x_curr);         % iteracion (raiz de 2)
end
fprintf('\nRaiz de 2 ~= %.8f en %d iteraciones (erp < %.0e)\n', x_curr, k, tol);

function [ea, er] = errores(x_real, x_aprox)
    ea = abs(x_aprox - x_real);
    er = ea / abs(x_real);
end
