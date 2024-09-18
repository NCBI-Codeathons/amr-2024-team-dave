/*
Subworkflow for doanloading of mutiple AMR databases


*/

include { CARD_DB as CARD_DB } from '../modules/CARD_DB.nf'


workflow VARIANT_CALLING {

    take:
        ch_ref         //    channel: [fasta]
        ch_genomes        //    channel: (sample, fasta)

    main:

        CARD_ONT_BWT(reads, ch_card_db)

    //emit:

}