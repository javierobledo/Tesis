/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package utils;

import java.io.File;
import java.io.IOException;
import cc.mallet.topics.tui.DMRLoader;

/**
 *
 * @author jrobledo
 */
public class LoadDMRInstances {
    public static void loadInstances(String features, String words, String instances) throws IOException{

        try{
            File instancesFile = new File(instances);
            DMRLoader loader = new DMRLoader();
            if(!fileExist(instancesFile)){
                if(words!= null && features!= null){
                    File wordsFile = new File(words);
                    File featuresFile = new File(features);
                    if(fileExist(wordsFile) && fileExist(featuresFile)){
                        loader.load(wordsFile, featuresFile, instancesFile);
                    }else{
                        if(!fileExist(wordsFile))System.err.print("The words file doesn't exist\n");
                        if(!fileExist(wordsFile))System.err.print("The features file doesn't exist\n");
                    }
            }else{
                System.err.print("The words or features file are not specified\n");
                throw new IOException();
            }
            
        }
        }catch(java.lang.NullPointerException e){
            System.err.print("You should specify an instance filename (use command -i)\n");
            System.exit(1);
        }
        
    }
    
    public static boolean fileExist(File f){
        return (f.exists() && !f.isDirectory());
    }
}
