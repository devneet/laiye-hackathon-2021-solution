import java.awt.Robot;
import java.awt.Toolkit;
import java.awt.Rectangle;
import java.awt.AWTException;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import javax.imageio.ImageIO;

public class ScreenshotPlugin{

    public static final long serialVersionUID = 1L;

    public void captureScreenshot(String filePath, String extenstion) throws InterruptedException, AWTException, IOException {

        Thread.sleep(120);
        Robot r = new Robot();

        // Used to get ScreenSize and capture image
        Rectangle capture = new Rectangle(Toolkit.getDefaultToolkit().getScreenSize());
        BufferedImage Image = r.createScreenCapture(capture);
        ImageIO.write(Image, extenstion, new File(filePath));
        System.out.println("Screenshot saved");
    }
/*
    public static void main(String[] args) throws InterruptedException, AWTException, IOException {

        ScreenshotPlugin plugin = new ScreenshotPlugin();
        plugin.captureScreenshot("D:\\Test.png","png");

    }
*/
}
