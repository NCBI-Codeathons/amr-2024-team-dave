process GUNZIP {
    label 'ultralow'

    input:
        tuple val(sample), file(fasta)

    output:
        tuple val(sample), path("temp/${sample}.fasta"), emit: decomp

    script:

    """
    mkdir temp
    mv ${fasta} temp/${sample}.fasta.gz
    gunzip -f temp/${sample}.fasta.gz
    """
}