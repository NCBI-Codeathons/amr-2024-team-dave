process PROKKA {
    label 'ultralow'
    container 'staphb/prokka:1.14.6'

    input:
        tuple val(sample), file(fasta)
    output:
        tuple val(sample), path("${sample}.faa"), emit: amino_acids
        tuple val(sample), path("${sample}.txt"), emit: summary

    script:

    """
    prokka --outdir output --prefix ${sample} ${fasta} --cpus ${task.cpus} --centre X --compliant
    cp ./output/*.faa ./${sample}.faa
    cp ./output/*.txt ./${sample}.txt
    """
}