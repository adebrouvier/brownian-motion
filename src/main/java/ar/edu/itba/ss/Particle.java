package ar.edu.itba.ss;

public class Particle {

    private int id;
    private double x;
    private double y;
    private double vx;
    private double vy;
    private double mass;
    private double radius;
    private CollisionType collision;

    public enum CollisionType {HORIZONTAL_WALL, VERTICAL_WALL, PARTICLE};

    public Particle(int id, double x, double y, double vx, double vy, double mass, double radius) {
        this.id = id;
        this.x = x;
        this.y = y;
        this.vx = vx;
        this.vy = vy;
        this.mass = mass;
        this.radius = radius;
    }

    public int getId() {
        return id;
    }

    public double getX() {
        return x;
    }

    public double getY() {
        return y;
    }

    public double getVx() {
        return vx;
    }

    public double getVy() {
        return vy;
    }

    public double getMass() {
        return mass;
    }

    public double getRadius() {
        return radius;
    }

    public void setX(double x) {
        this.x = x;
    }

    public void setY(double y) {
        this.y = y;
    }

    public void setVx(double vx) {
        this.vx = vx;
    }

    public void setVy(double vy) {
        this.vy = vy;
    }

    public CollisionType getCollision() {
        return collision;
    }

    public void setCollision(CollisionType collision) {
        this.collision = collision;
    }

    @Override
    public String toString() {
        return "Particle{" +
                "id=" + id +
                ", x=" + x +
                ", y=" + y +
                ", vx=" + vx +
                ", vy=" + vy +
                ", mass=" + mass +
                ", radius=" + radius +
                ", collision=" + collision +
                '}';
    }
}
