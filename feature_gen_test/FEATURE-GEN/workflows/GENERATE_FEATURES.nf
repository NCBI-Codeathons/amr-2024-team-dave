/*
~~~~~~~~~~~~~~~~~~~~~~
Importing subworkflows
~~~~~~~~~~~~~~~~~~~~~~
*/

include { VARIANT_CALLING as VARIANT_CALLING } from '../subworkflows/VARIANT_CALLING.nf'
include { GENE_CALLING as GENE_CALLING } from '../subworkflows/GENE_CALLING.nf'



workflow GENERATE_FEATURES {
    take:
        ch_ref         //    channel: [fasta]
        ch_genomes        //    channel: (sample, fasta)

    main:




/*
###################################################################################
####################### Whole Process #############################################
###################################################################################
*/


    VARIANT_CALLING(ch_ref, ch_genomes)

    GENE_CALLING(ch_ref, ch_genomes)

}