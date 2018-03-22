package ar.edu.itba.ss;

import java.util.ArrayList;
import java.util.List;

public class BrownianMotion{

    /* Small Particles */
    private static double R1 = 0.005;
    private static double M1 = 0.1;
    private static double V1 = 0.1;

    /* Big Particle */
    private static double R2 = 0.05;
    private static double M2 = 100;

    private static double L = 0.5;

    public static void main( String[] args ){
        CliParser.parseOptions(args);
        List<Particle> particles = generateParticles();
        brownianMotion(particles);
    }

    private static List<Particle> generateParticles() {
        List<Particle> particles = new ArrayList<>();

        /* Add big particle */
        particles.add(new Particle(1, randomCoord(R2), randomCoord(R2), 0, 0, M2, R2));

        for (int i = 0; i < CliParser.numberOfParticles; i++){

            double x;
            double y;

            do {
                x = randomCoord(R1);
                y = randomCoord(R1);
            }
            while (!validCords(x,y, particles));

            particles.add(new Particle(i+2, x, y, randomSpeed(), randomSpeed(), M1, R1));
        }

        return particles;
    }

    private static void brownianMotion(List<Particle> particles) {

        for (int i = 0; i < 1; i++){
            double tc = Double.POSITIVE_INFINITY;
            Particle pi = null;
            Particle pj = null;
            for (Particle particle : particles){ /* Find next collision time (tc) */

                double verticalTc = getVWallTime(particle);
                double horizontalTc = getHWallTime(particle);

                if (verticalTc < tc){
                    tc = verticalTc;
                    particle.setCollision(Particle.CollisionType.VERTICAL_WALL);
                    pi = particle;
                    pj = null;
                }

                if (horizontalTc < tc) {
                    tc = horizontalTc;
                    particle.setCollision(Particle.CollisionType.HORIZONTAL_WALL);
                    pi = particle;
                    pj = null;
                }

                /* Particle collision */
                for (Particle otherParticle : particles){
                    if (particle.getId() != otherParticle.getId()){

                        double dX = otherParticle.getX() - particle.getX();
                        double dY = otherParticle.getY() - particle.getY();
                        double dVx = otherParticle.getVx() - particle.getVx();
                        double dVy = otherParticle.getVy() - particle.getVy();

                        double dVdR = dVx*dX + dVy*dY;

                        if (dVdR  >= 0){
                            continue;
                        }

                        double dVdV = Math.pow(dVx, 2) + Math.pow(dVy, 2);

                        double dRdR = Math.pow(dX, 2) + Math.pow(dY, 2);

                        double sigma = particle.getRadius() + otherParticle.getRadius();

                        double d = Math.pow(dVdR, 2) - dVdV * (dRdR - Math.pow(sigma ,2));

                        if (d < 0){
                            continue;
                        }

                        double ptc = (-1) * (dVdR + Math.sqrt(d)) / dVdV;

                        if (ptc < tc){
                            tc = ptc;
                            particle.setCollision(Particle.CollisionType.PARTICLE);
                            pi = particle;
                            pj = otherParticle;
                        }
                    }
                }
            }

            updatePosition(particles, tc);

            updateSpeed(pi, pj);

            System.out.println("tc: " + tc + " - " + pi.toString());
        }
    }

    /**
     * Obtains the time in which a particle collides against a vertical wall.
     * @param particle particle to get the time.
     * @return time of collision.
     */
    private static double getVWallTime(Particle particle) {

        if (particle.getVx() > 0) {
            return (L - particle.getRadius() - particle.getX()) / particle.getVx();
        } else if (particle.getVx() < 0) {
            return (0 + particle.getRadius() - particle.getX()) / particle.getVx();
        }

        return Double.POSITIVE_INFINITY;
    }

    /**
     * Obtains the time in which a particle collides against an horizontal wall.
     * @param particle particle to get the time.
     * @return time of collision.
     */
    private static double getHWallTime(Particle particle) {
        if (particle.getVy() > 0){
            return  (L - particle.getRadius() - particle.getY()) / particle.getVy();
        }else if (particle.getVy() < 0){
            return  (0 + particle.getRadius() - particle.getY())  / particle.getVy();
        }

        return Double.POSITIVE_INFINITY;
    }

    /**
     * Checks if there is already a particle on that coordinates.
     * @param x coordinate to check.
     * @param y coordinate to check.
     * @param particles list of particles in the cell.
     * @return true if there is already a particle on the given coordinates, false otherwise.
     */
    private static boolean validCords(double x, double y, List<Particle> particles) {

        for (Particle p: particles){
            boolean valid = Math.pow(p.getX() - x, 2) + Math.pow(p.getY() - y, 2) > Math.pow(p.getRadius() + R1, 2);
            if (!valid){
                return false;
            }
        }

        return true;
    }

    /**
     * Obtain a random speed on a given interval
     * @return a speed on the interval (-V1, V1)
     */
    private static double randomSpeed(){
        return  2 * V1 * Math.random() - V1;
    }

    /**
     * Returns a random coordinate between the radius and L - radius.
     * @param radius radius of the particle.
     * @return a coordinate in the (radius, L - radius) interval.
     */
    private static double randomCoord(double radius){
        return  radius + (L - 2 * radius) * Math.random();
    }

    /**
     * Updates the speed of the particle/s that collided.
     * @param pi first particle
     * @param pj second particle
     */
    private static void updateSpeed(Particle pi, Particle pj) {

        if (pi.getCollision() == Particle.CollisionType.VERTICAL_WALL) {
            pi.setVx(pi.getVx() * (-1));
            return;
        }

        if (pi.getCollision() == Particle.CollisionType.HORIZONTAL_WALL) {
            pi.setVy(pi.getVy() * (-1));
            return;
        }

        if (pi.getCollision() == Particle.CollisionType.PARTICLE){

            double dX = pj.getX() - pi.getX();
            double dY = pj.getY() - pi.getY();
            double dVx = pj.getVx() - pi.getVx();
            double dVy = pj.getVy() - pi.getVy();

            double dVdR = dVx*dX + dVy*dY;
            double sigma = pi.getRadius() + pj.getRadius();

            double J = 2*pi.getMass()*pj.getMass()*dVdR / sigma * (pi.getMass() + pj.getMass());
            double Jx = J * dX / sigma;
            double Jy = J * dY / sigma;

            pi.setVx(pi.getVx() + Jx/pi.getMass());
            pi.setVy(pi.getVy() + Jy/pi.getMass());

            pj.setVx(pj.getVx() + Jx/pj.getMass());
            pj.setVy(pj.getVy() + Jy/pj.getMass());
        }

    }

    /**
     * Evolve the system by updating the particles positions.
     * @param particles list of particles.
     * @param tc time of the collision.
     */
    private static void updatePosition(List<Particle> particles, double tc) {

        for (Particle particle : particles){
            particle.setX(particle.getX() + particle.getVx() * tc);
            particle.setY(particle.getY() + particle.getVy() * tc);
        }

    }
}
