/*
Subworkflow for calling variants between test genomes and a reference genomes


*/

include { MUMMER as MUMMER } from '../modules/MUMMER.nf'


workflow VARIANT_CALLING {

    take:
        ch_ref         //    channel: (sample, reference)
        ch_genomes        //    channel: (sample, fasta)

    main:

        ch_for_mummer = ch_genomes.join(ch_ref)

        MUMMER(ch_for_mummer)

    //emit:

}