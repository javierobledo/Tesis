/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ldamallet;

import cc.mallet.topics.DMRTopicModel;
import cc.mallet.types.InstanceList;
import java.io.File;
import java.io.IOException;
import utils.CommandLineArgsParser;
import utils.LoadDMRInstances;
import java.util.HashMap;

/**
 *
 * @author jrobledo
 */
public class LDAMallet {
    
    //IMPORTANTE: Fijarse en para que sirven los demas parametros de DMR

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args){
        // TODO code application logic here
        HashMap<String,Object> commands = CommandLineArgsParser.processCommandLineArgs(args);
        String type = (String)commands.get("type");
        if(type != null){
            switch(type){
                case "dmr":
                    System.out.print("DMR!");
                    String instancesFile = (String)commands.get("i");
                    String wordsFile = (String)commands.get("w");
                    String featuresFile = (String)commands.get("f");
                    String k = (String)commands.get("k");
                    try{
                        LoadDMRInstances.loadInstances(featuresFile, wordsFile, instancesFile);
                    }catch(IOException e){
                    }catch(NullPointerException e){
                    }
                    DMR dmr = new DMR(Integer.parseInt(k));
                    try{
                        dmr.classify(instancesFile, "hola");
                    }catch(IOException e){
                        
                    }
                    break;
                case "lda":
                    System.out.print("LDA!");
                    break;
                default:
                    System.err.print("Type of LDA algorithm not supported");
            }
        }else{
            System.err.print("type parameter missing\n");
            System.exit(1);
        }
    }
    
}
