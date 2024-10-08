process NUC_FEATURES {
    label 'ultralow'
    container 'ebird013/feature_gen:0.2'

    input:
        tuple val(sample), file(fasta)
    output:
        tuple val(sample), path("${sample}_nuc_feat.csv"), emit: nuc_features

    script:

    """
    mkdir output
    python /home/amr-2024-team-dave/feature_gen_lib/main.py -m nuc_feat -f ${fasta} -o output
    cp ./output/*.csv ./${sample}_nuc_feat.csv
    """
}

process PRO_FEATURES {
    label 'ultralow'
    container 'ebird013/feature_gen:0.2'

    input:
        tuple val(sample), file(fasta)
    output:
        tuple val(sample), path("${sample}_aa_feat.csv"), emit: nuc_features

    script:

    """
    mkdir output
    python /home/amr-2024-team-dave/feature_gen_lib/main.py -m pro_feat -p ${fasta} -o output
    cp ./output/*.csv ./${sample}_aa_feat.csv
    """
}

process FETCH_GENOME {
    label 'ultralow'
    container 'ebird013/feature_gen:0.2'
    maxForks 1
    errorStrategy 'retry'

    input:
        tuple val(sample), val(acc)
    output:
        tuple val(sample), path("${acc}.fasta.gz"), emit: genome

    script:

    """
    mkdir output
    python /home/amr-2024-team-dave/feature_gen_lib/main.py -m fetch -a ${acc} -e ${params.email} -o output
    cp output/*.gz ./${acc}.fasta.gz
    """
}

process REMOVE_GUIDED {
    label 'ultralow'
    container 'ebird013/feature_gen:0.2'

    input:
        tuple val(sample), file(fasta)
    output:
        tuple val(sample), path("${sample}.fasta"), emit: denovo

    script:

    """
    mkdir output
    python /home/amr-2024-team-dave/feature_gen_lib/main.py -m remove_guided -f ${fasta} -o output
    cp output/*.fasta ./${sample}.fasta
    """
}

process MUMMER_PARSE {
    label 'ultralow'
    container 'ebird013/feature_gen:0.2'

    input:
        tuple val(sample), file(mum_out)
    output:
        tuple val(sample), path("${sample}_mummer.csv"), emit: mummer_parse

    script:

    """
    python /home/amr-2024-team-dave/feature_gen_lib/main.py -m mummer_parse -i ${mum_out} -o ${sample}_mummer.csv
    """
}

process PROKKA_PARSE {
    label 'ultralow'
    container 'ebird013/feature_gen:0.2'

    input:
        tuple val(sample), file(pro_out)
    output:
        tuple val(sample), path("${sample}_prokka.csv"), emit: prokka_parse

    script:

    """
    python /home/amr-2024-team-dave/feature_gen_lib/main.py -m prokka_parse -i ${pro_out} -o ${sample}_prokka.csv
    """
}
