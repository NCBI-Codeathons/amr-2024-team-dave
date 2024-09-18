/*
A subworkflows for calling genes from test genomes and a reference genomes

*/

include { PROKKA as PROKKA_TEST_SET } from '../modules/PROKKA.nf'
include { PROKKA as PROKKA_REF_SET } from '../modules/PROKKA.nf'


workflow GENE_CALLING {

    take:
        ch_ref         //    channel: (sample, reference)
        ch_genomes        //    channel: (sample, fasta)

    main:

        PROKKA_TEST_SET(ch_genomes)

        PROKKA_REF_SET(ch_ref)

    //emit:

}