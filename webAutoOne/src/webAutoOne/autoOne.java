package webAutoOne;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.support.ui.WebDriverWait;

//import webAutoOne.InterruptedException;
//import WebAutoOne.String;

import java.util.concurrent.TimeUnit;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.chrome.ChromeDriver;


public class autoOne {
	public static void main(String[] args) throws InterruptedException {
        // declaration and instantiation of objects/variables
    	//System.setProperty("webdriver.gecko.driver","C:\\geckodriver.exe");
		//WebDriver driver = new FirefoxDriver();
		//comment the above 2 lines and uncomment below 2 lines to use Chrome
		System.setProperty("webdriver.chrome.driver","/Users/seanxu/eclipse-workspace/chromedriver");
		WebDriver driver = new ChromeDriver();
    	
        String baseUrl = "http://demo.guru99.com/test/newtours/";
        // launch Fire fox and direct it to the Base URL
        driver.get(baseUrl);
        //driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
        //driver.manage().timeouts().pageLoadTimeout(30, TimeUnit.SECONDS);
        Thread.sleep(5000); //wait 5 sec
        
        String expectedTitle = "Welcome: Mercury Tours";
        String actualTitle = "";
        // get the actual value of the title
        actualTitle = driver.getTitle();

        /*
         * compare the actual title of the page with the expected one and print
         * the result as "Passed" or "Failed"
         */
        if (actualTitle.contentEquals(expectedTitle)){
            System.out.println("Test Passed!");
        } else {
            System.out.println("Test Failed");
        }
       
        //close browser
        driver.close();
       
    }
}
