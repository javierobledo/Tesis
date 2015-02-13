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

/**
 *
 * @author jrobledo
 */
public class DMR {
    
    private int k;

    public DMR(int k) {
        this.k = k;
    }
    
    public void classify(String filename, String output) throws IOException{
        InstanceList training = InstanceList.load (new File(filename));
        DMRTopicModel lda = new DMRTopicModel(k);
                lda.setOptimizeInterval(100);
                lda.setTopicDisplay(100, 10);
                lda.addInstances(training);
                lda.estimate();
                lda.writeParameters(new File(output+"_dmr.parameters"));
                lda.printState(new File(output+"_dmr.state.gz"));
    }
    
}
