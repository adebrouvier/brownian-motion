function histogram(filename)

  [N,x,y,vx,vy,r,tc] = parse(filename);
  time = 0;
  particle = 0;
  for i = 1:columns(x)
    if particle != N
      particle += 1;
      continue;
    endif
    time += tc(i);
    particle = 0;
    frequencies(end + 1) = time;
  endfor
  hist(frequencies, ceil(time));

endfunction