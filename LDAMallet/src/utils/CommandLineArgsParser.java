/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package utils;
import java.util.HashMap;
/**
 *
 * @author jrobledo
 */
public class CommandLineArgsParser {
    
    public static HashMap processCommandLineArgs(String[] args){
        HashMap commands = new HashMap();
        for(int i = 0; i < args.length; i++){
            if(args[i].charAt(0) == '-'){
                commands.put(args[i].substring(1), args[i+1]);
            }
        }
        return commands;
    }
    
}
