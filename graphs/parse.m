function [N, x,y,vx,vy,r,tc] = parse(filename)
  file = fopen(filename, "r");
  while !feof(file)
    N = str2num(fgetl(file));
    fgetl(file);
    for i = 1:N-2
      line = fgetl(file);
      [x(end+1) y(end+1) vx(end+1) vy(end+1) r(end+1) tc(end+1)] = sscanf(line, "%f %f %f %f %f %f", "C");
    endfor
    fgetl(file);
    fgetl(file);
  endwhile
  N -= 2;
endfunction