from django.db import models
from django_mysql.models import *
# Create your models here.

#i_idcons = models.IntegerField(primary_key=True, db_column = "i_idcons")

class IVistaGenPteInfo(models.Model):
    i_idcons = models.IntegerField(primary_key=True, db_column = "i_idcons")
    s_nombpuente = models.CharField(max_length=100)
    s_idpuente = models.CharField(max_length=25)
    s_idsipucol = models.CharField(max_length=25, blank=True, null=True)
    s_territ = models.CharField(max_length=50, blank=True, null=True)
    i_tipocarr = models.IntegerField()
    s_idcarr = models.CharField(max_length=10)
    s_nomtramo = models.CharField(max_length=100)
    s_adminvial = models.CharField(max_length=100, blank=True, null=True)
    i_sentpuente = models.IntegerField()
    p_senalidpuen = models.CharField(max_length=500, blank=True, null=True)
    i_obstaculo = models.IntegerField()
    p_obstaculo = models.CharField(max_length=500, blank=True, null=True)
    p_entorno = models.CharField(max_length=500, blank=True, null=True)
    s_carrsalva = models.CharField(max_length=10, blank=True, null=True)
    s_cuerpoagua = models.CharField(max_length=100, blank=True, null=True)
    i_anoconstr = models.IntegerField(blank=True, null=True)
    d_latgra = models.DecimalField(max_digits=10, decimal_places=6)
    d_latmin = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    d_latseg = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    d_longra = models.DecimalField(max_digits=10, decimal_places=6)
    d_lonmin = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    d_lonseg = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    s_lon = models.CharField(max_length=20)
    s_absi = models.CharField(max_length=10)
    i_absikm = models.IntegerField()
    s_absf = models.CharField(max_length=10)
    i_absfkm = models.IntegerField()
    i_absfmm = models.IntegerField()
    b_infcantsup = models.TextField(blank=True, null=True)  # This field type is a guess.
    d_supconcr = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    d_suprefact = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    d_suprefpas = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    d_supacero = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    b_infcantsub = models.TextField(blank=True, null=True)  # This field type is a guess.
    d_subconcr = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    d_subref = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    d_subacero = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    d_subareaaf = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    b_infcantcim = models.TextField(blank=True, null=True)  # This field type is a guess.
    d_cimconcr = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    d_cimref = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    d_cimmamp = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    b_infcappres = models.TextField(blank=True, null=True)  # This field type is a guess.
    d_costdis = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    d_costprelim = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    d_costpav = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    d_costpubli = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    d_costestr = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    d_costhidr = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    d_costredes = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    d_costgest = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    d_costadic = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    d_costtotal = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    d_valrepos = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    i_tipolgen = models.IntegerField(blank=True, null=True)
    p_genpuente = models.CharField(max_length=500, blank=True, null=True)
    p_planta = models.CharField(max_length=500, blank=True, null=True)
    p_perfil = models.CharField(max_length=500, blank=True, null=True)
    b_amplmod = models.CharField(max_length=10, blank=True, null=True)
    b_reforz = models.CharField(max_length=10, blank=True, null=True)
    b_pasarela = models.CharField(max_length=10, blank=True, null=True)
    d_wtotal = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_ltotal = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_areaplan = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_galsup1 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_galinf1 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_galhor1 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_galsup2 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_galinf2 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_galhor2 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_wcarr1 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_wcarr2 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_wcalz1 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_wcalz2 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_wberma1 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_wberma2 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    p_gencalzada = models.CharField(max_length=500, blank=True, null=True)
    d_numcalzbajo = models.IntegerField(blank=True, null=True)
    d_numcarrbajo = models.IntegerField(blank=True, null=True)
    i_matsuprod = models.IntegerField(blank=True, null=True)
    d_wsuprod = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_lsuprod = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_tsuprod = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    b_border = models.CharField(max_length=100, blank=True, null=True)
    d_wborder = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_lborder = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_hborder = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    b_borizq = models.CharField(max_length=100, blank=True, null=True)
    d_wborizq = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_lborizq = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_hborizq = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    b_barder = models.CharField(max_length=100, blank=True, null=True)
    i_confbarder = models.IntegerField(blank=True, null=True)
    d_bbarder = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_lbarder = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_hbarder = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    p_barder = models.CharField(max_length=500, blank=True, null=True)
    b_barizq = models.CharField(max_length=100, blank=True, null=True)
    i_confbarizq = models.IntegerField(blank=True, null=True)
    d_bbarizq = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_hbarizq = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_lbarizq = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    p_barizq = models.CharField(max_length=500, blank=True, null=True)
    b_andder = models.CharField(max_length=100, blank=True, null=True)
    i_matandder = models.IntegerField(blank=True, null=True)
    d_wandder = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_landder = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_handder = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    b_andizq = models.CharField(max_length=100, blank=True, null=True)
    i_matandizq = models.IntegerField(blank=True, null=True)
    d_wandizq = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_landizq = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_handizq = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    b_cerram = models.CharField(max_length=100, blank=True, null=True)
    b_separ = models.CharField(max_length=100, blank=True, null=True)
    i_matsepar = models.IntegerField(blank=True, null=True)
    d_bsepar = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_lsepar = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_hsepar = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    b_dren = models.CharField(max_length=100, blank=True, null=True)
    b_ilum = models.CharField(max_length=100, blank=True, null=True)
    d_tefpuente = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_tarriba = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_tabajo = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    p_caucearriba = models.CharField(max_length=500, blank=True, null=True)
    p_cauceagabajo = models.CharField(max_length=500, blank=True, null=True)
    i_afluent = models.IntegerField(blank=True, null=True)
    d_disaflar = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_disaflab = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    i_tipmatcanal = models.IntegerField(blank=True, null=True)
    b_unimatcanal = models.TextField(blank=True, null=True)  # This field type is a guess.
    p_matcanal = models.CharField(max_length=500, blank=True, null=True)
    i_tipmatizq = models.IntegerField(blank=True, null=True)
    b_unimatizq = models.TextField(blank=True, null=True)  # This field type is a guess.
    p_matizq = models.CharField(max_length=500, blank=True, null=True)
    i_tipmatder = models.IntegerField(blank=True, null=True)
    b_unimatder = models.TextField(blank=True, null=True)  # This field type is a guess.
    p_matder = models.CharField(max_length=500, blank=True, null=True)
    i_tipmatbarsed = models.IntegerField(blank=True, null=True)
    b_unimatbarsed = models.TextField(blank=True, null=True)  # This field type is a guess.
    p_matbarsed = models.CharField(max_length=500, blank=True, null=True)
    i_estrhidr = models.IntegerField(blank=True, null=True)
    i_estreros = models.IntegerField(blank=True, null=True)
    i_estrinund = models.IntegerField(blank=True, null=True)
    i_estrconagua = models.IntegerField(blank=True, null=True)
    i_ubictalud = models.IntegerField(blank=True, null=True)
    p_taludpuente = models.CharField(max_length=500, blank=True, null=True)
    i_numaptalud = models.IntegerField(blank=True, null=True)
    p_aptalud = models.CharField(max_length=500, blank=True, null=True)
    i_tipmatlad = models.IntegerField(blank=True, null=True)
    i_pendtalud = models.IntegerField(blank=True, null=True)
    i_htalud = models.IntegerField(blank=True, null=True)
    i_vegtalud = models.IntegerField(blank=True, null=True)
    b_estrtalud = models.TextField(blank=True, null=True)  # This field type is a guess.
    i_tipestrtalud = models.IntegerField(blank=True, null=True)
    d_hesttalud = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_lesttalud = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    i_numterraz = models.IntegerField(blank=True, null=True)
    p_estrtalud = models.CharField(max_length=500, blank=True, null=True)
    b_regfotos = models.TextField(blank=True, null=True)  # This field type is a guess.
    s_rutafotos = models.CharField(max_length=500, blank=True, null=True)
    b_esquemas = models.TextField(blank=True, null=True)  # This field type is a guess.
    s_rutaesquemas = models.CharField(max_length=500, blank=True, null=True)
    b_planplanta = models.TextField(blank=True, null=True)  # This field type is a guess.
    b_planperfil = models.TextField(blank=True, null=True)  # This field type is a guess.
    b_plansecc = models.TextField(blank=True, null=True)  # This field type is a guess.
    b_plandetal = models.TextField(blank=True, null=True)  # This field type is a guess.
    b_planconstr = models.TextField(blank=True, null=True)  # This field type is a guess.
    b_planasbui = models.TextField(blank=True, null=True)  # This field type is a guess.
    s_rutaplanos = models.CharField(max_length=500, blank=True, null=True)
    b_contrdis = models.TextField(blank=True, null=True)  # This field type is a guess.
    b_contrconstr = models.TextField(blank=True, null=True)  # This field type is a guess.
    b_contrsuper = models.TextField(blank=True, null=True)  # This field type is a guess.
    b_contrmant = models.TextField(blank=True, null=True)  # This field type is a guess.
    b_contrinterv = models.TextField(blank=True, null=True)  # This field type is a guess.
    s_rutacontratos = models.CharField(max_length=500, blank=True, null=True)
    s_disenador = models.CharField(max_length=200, blank=True, null=True)
    s_constructor = models.CharField(max_length=200, blank=True, null=True)
    s_supervinterv = models.CharField(max_length=200, blank=True, null=True)
    b_memodis = models.TextField(blank=True, null=True)  # This field type is a guess.
    s_rutamemodis = models.CharField(max_length=500, blank=True, null=True)
    b_memocost = models.TextField(blank=True, null=True)  # This field type is a guess.
    s_rutamemocost = models.CharField(max_length=500, blank=True, null=True)
    b_memointerv = models.TextField(blank=True, null=True)  # This field type is a guess.
    s_rutamemoint = models.CharField(max_length=500, blank=True, null=True)
    b_estsuelos = models.TextField(blank=True, null=True)  # This field type is a guess.
    b_esthidro = models.TextField(blank=True, null=True)  # This field type is a guess.
    b_estcapcarga = models.TextField(blank=True, null=True)  # This field type is a guess.
    b_estvulsismo = models.TextField(blank=True, null=True)  # This field type is a guess.
    b_estvulsocav = models.TextField(blank=True, null=True)  # This field type is a guess.
    s_rutaesting = models.CharField(max_length=500, blank=True, null=True)
    t_fechaconstr = models.DateField(blank=True, null=True)
    t_fechaultinsp = models.DateField(blank=True, null=True)
    b_mantenim = models.TextField(blank=True, null=True)  # This field type is a guess.
    t_fechaultmant = models.DateField(blank=True, null=True)
    b_interv = models.TextField(blank=True, null=True)  # This field type is a guess.
    t_fechaultinter = models.DateField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'i_vista_gen_pte_info'


class IEstApoyoInterno(models.Model):
    i_idcons = models.ForeignKey(IVistaGenPteInfo, on_delete=models.CASCADE, db_column="i_idcons")
    s_idpuente = models.CharField(max_length=25)
    i_idejecons = models.IntegerField()
    i_ideje = models.DecimalField(max_digits=3, decimal_places=1)
    i_matapoyint = models.IntegerField()
    i_tipapoyint = models.IntegerField()
    i_tipsecapoyint = models.IntegerField()
    b_capitel = models.TextField(blank=True, null=True)  # This field type is a guess.
    b_vigcabez = models.TextField(blank=True, null=True)  # This field type is a guess.
    b_vigtrans = models.TextField(blank=True, null=True)  # This field type is a guess.
    p_apoyintsup = models.CharField(max_length=500, blank=True, null=True)
    p_apoyintinf = models.CharField(max_length=500, blank=True, null=True)
    b_encauceapint = models.TextField(blank=True, null=True)  # This field type is a guess.
    i_tipcimapoyint = models.IntegerField(blank=True, null=True)
    i_estrsocav = models.IntegerField(blank=True, null=True)
    i_estrasent = models.IntegerField(blank=True, null=True)
    i_numpilmur = models.IntegerField()
    d_stranpil = models.DecimalField(max_digits=10, decimal_places=4)
    i_geomapoyint = models.IntegerField()
    d_longapoyint = models.DecimalField(max_digits=10, decimal_places=4)
    d_dimtranapoyint = models.DecimalField(max_digits=10, decimal_places=4)
    d_dimlongapoyint = models.DecimalField(max_digits=10, decimal_places=4)
    d_recapoyint = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_hapoyint = models.DecimalField(max_digits=10, decimal_places=4)
    d_bvigcabez = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_hvigcabez = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_bvigtrans = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_hvigtrans = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    i_esvapoyint = models.IntegerField(blank=True, null=True)
    i_inclvapoyint = models.IntegerField(blank=True, null=True)
    d_lzapcim = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_bzapcim = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_dzapcim = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    i_numpil = models.IntegerField(blank=True, null=True)
    b_llavextapoyint = models.TextField()  # This field type is a guess.
    b_llavintapoyint = models.TextField()  # This field type is a guess.
    d_btopsis = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_htopsis = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_tsuptopsis = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_tinftopsis = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    b_tirantes = models.TextField()  # This field type is a guess.
    p_tirantepil = models.CharField(max_length=500, blank=True, null=True)
    p_tirantetab = models.CharField(max_length=500, blank=True, null=True)
    b_tensores = models.TextField()  # This field type is a guess.
    p_tensorsup = models.CharField(max_length=500, blank=True, null=True)
    p_tensortab = models.CharField(max_length=500, blank=True, null=True)
    b_pendolo = models.TextField()  # This field type is a guess.
    p_pendolo = models.CharField(max_length=500, blank=True, null=True)
    b_macizos = models.TextField()  # This field type is a guess.
    p_macizos = models.CharField(max_length=500, blank=True, null=True)
    i_numtirantes = models.IntegerField(blank=True, null=True)
    i_numtensores = models.IntegerField(blank=True, null=True)
    i_numpendol = models.IntegerField(blank=True, null=True)
    i_nummacizos = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'i_est_apoyo_interno'
        unique_together = (('i_idcons', 'i_idejecons'),)



class IEstElementoSuperestructura(models.Model):
    i_idcons = models.IntegerField(primary_key=True, db_column="i_idcons")
    s_idpuente = models.CharField(max_length=25)
    i_idluzcons = models.IntegerField(blank=True, null=True)
    i_idluz = models.DecimalField(max_digits=3, decimal_places=1)
    b_supermix = models.TextField()  # This field type is a guess.
    i_matsistran = models.IntegerField()
    i_metodcons = models.IntegerField(blank=True, null=True)
    i_estrtrans = models.IntegerField()
    p_estrtrans = models.CharField(max_length=500, blank=True, null=True)
    i_contapoyoi = models.IntegerField()
    i_tipoapoyoi = models.IntegerField()
    p_apoyoi = models.CharField(max_length=500, blank=True, null=True)
    i_contapoyof = models.IntegerField()
    i_tipoapoyof = models.IntegerField()
    p_apoyof = models.CharField(max_length=500, blank=True, null=True)
    i_matlosa = models.IntegerField()
    i_tiplosa = models.IntegerField()
    b_voladizq = models.TextField(blank=True, null=True)  # This field type is a guess.
    b_voladder = models.TextField(blank=True, null=True)  # This field type is a guess.
    b_diafragi = models.TextField(blank=True, null=True)  # This field type is a guess.
    b_diafragf = models.TextField(blank=True, null=True)  # This field type is a guess.
    i_tipodiafragi = models.IntegerField(blank=True, null=True)
    i_tipodiafragf = models.IntegerField(blank=True, null=True)
    i_tipoarrtrans = models.IntegerField(blank=True, null=True)
    i_tipoarrlong = models.IntegerField(blank=True, null=True)
    i_tipoelevert = models.IntegerField(blank=True, null=True)
    i_tipodiago = models.IntegerField(blank=True, null=True)
    i_tiposecordsup = models.IntegerField(blank=True, null=True)
    i_tiposecordinf = models.IntegerField(blank=True, null=True)
    i_tiposemont = models.IntegerField(blank=True, null=True)
    b_mensvigi = models.TextField(blank=True, null=True)  # This field type is a guess.
    b_mensvigf = models.TextField(blank=True, null=True)  # This field type is a guess.
    b_refextvig = models.TextField(blank=True, null=True)  # This field type is a guess.
    b_curv = models.TextField(blank=True, null=True)  # This field type is a guess.
    d_lluz = models.DecimalField(max_digits=10, decimal_places=4)
    d_hlosa = models.DecimalField(max_digits=10, decimal_places=4)
    d_wvoladizq = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_wvoladder = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    i_numvigas = models.IntegerField()
    i_tipsecvig = models.IntegerField()
    i_numriost = models.IntegerField(blank=True, null=True)
    i_numatstra = models.IntegerField(blank=True, null=True)
    i_numatslon = models.IntegerField(blank=True, null=True)
    i_numtramos = models.IntegerField(blank=True, null=True)
    i_numelemvert = models.IntegerField(blank=True, null=True)
    d_bmedvigasap = models.DecimalField(max_digits=10, decimal_places=4)
    d_hmedvigasap = models.DecimalField(max_digits=10, decimal_places=4)
    d_bsupvigasap = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_hsupvigasap = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_binfvigasap = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_hinfvigasap = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_bmedvigascl = models.DecimalField(max_digits=10, decimal_places=4)
    d_hmedvigascl = models.DecimalField(max_digits=10, decimal_places=4)
    d_bsupvigascl = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_hsupvigascl = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_binfvigascl = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_hinfvigascl = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_svigas = models.DecimalField(max_digits=10, decimal_places=4)
    d_lvigas = models.DecimalField(max_digits=10, decimal_places=4)
    d_tparedhuecv = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_recvigas = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_lsecapoy = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_lsectrans = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_lapefeci = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_hapefeci = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_gapi = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_lapefecf = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_hapefecf = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_gapf = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_bmedelem2ap = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_hmedelem2ap = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_bsupelem2ap = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_hsupelem2ap = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_binfelem2ap = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_hinfelem2ap = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_bmedelem2cl = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_hmedelem2cl = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_bsupelem2cl = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_hsupelem2cl = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_binfelem2cl = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_hinfelem2cl = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_selem2 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_lelem2 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_tparedhuec2 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_bmedelem3ap = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_hmedelem3ap = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_bsupelem3ap = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_hsupelem3ap = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_binfelem3ap = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_hinfelem3ap = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_bmedelem3cl = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_hmedelem3cl = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_bsupelem3cl = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_hsupelem3cl = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_binfelem3cl = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_hinfelem3cl = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_selem3 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_lelem3 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_tparedhuec3 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_bmedelem4ap = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_hmedelem4ap = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_bsupelem4ap = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_hsupelem4ap = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_binfelem4ap = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_hinfelem4ap = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_bmedelem4cl = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_hmedelem4cl = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_bsupelem4cl = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_hsupelem4cl = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_binfelem4cl = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_hinfelem4cl = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_selem4 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_lelem4 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_tparedhuec4 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    n_material_predom = models.IntegerField(blank=True, null=True)
    n_estr = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'i_est_elemento_superestructura'
        unique_together = (('i_idcons', 'i_idluzcons'),)


class IEstEstribo(models.Model):
    i_idcons = models.ForeignKey(IVistaGenPteInfo, on_delete=models.CASCADE, db_column="i_idcons")
    s_idpuente = models.CharField(max_length=25)
    i_idejecons = models.CharField(primary_key=True, max_length=100, blank=True, null=False)
    i_ideje = models.DecimalField(max_digits=3, decimal_places=1)
    i_tipestribo = models.IntegerField()
    i_matestribo = models.IntegerField()
    p_genestribo = models.CharField(max_length=500, blank=True, null=True)
    b_encauceestr = models.CharField(max_length=100, blank=True, null=True)
    i_esvestribo = models.IntegerField(blank=True, null=True)
    i_tipcimestr = models.IntegerField(blank=True, null=True)
    i_estrsocav = models.IntegerField(blank=True, null=True)
    i_estrasent = models.IntegerField(blank=True, null=True)
    d_hespald = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_bsilla = models.DecimalField(max_digits=10, decimal_places=4)
    d_hsilla = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_westribo = models.DecimalField(max_digits=10, decimal_places=4)
    d_lzapcim = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_bzapcim = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_dzapcim = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    i_numpil = models.IntegerField(blank=True, null=True)
    b_llavextestr = models.CharField(max_length=100)
    b_llavintestr = models.CharField(max_length=100)
    d_btopsis = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_htopsis = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_tsuptopsis = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_tinftopsis = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'i_est_estribo'
        unique_together = (('i_idcons', 'i_idejecons'),)


class IEstJunta(models.Model):
    i_consecid = models.IntegerField(primary_key=True)
    i_idjunt = models.IntegerField()
    i_tipjunt = models.IntegerField()
    d_posjunt = models.DecimalField(max_digits=10, decimal_places=4)
    d_ljunt = models.DecimalField(max_digits=10, decimal_places=4)
    d_bjunt = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    p_junt = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'i_est_junta'
        unique_together = (('i_consecid', 'i_idjunt'),)



class IOpeTransito(models.Model):
    i_idcons = models.IntegerField(primary_key=True, db_column="i_idcons")
    s_idpuente = models.CharField(max_length=25)
    i_idsent = models.IntegerField()
    b_senalident = models.TextField()  # This field type is a guess.
    b_angosto = models.TextField()  # This field type is a guess.
    b_sengalibo = models.TextField()  # This field type is a guess.
    d_sengalibo = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    b_capcarga = models.TextField()  # This field type is a guess.
    i_capcarga = models.IntegerField(blank=True, null=True)
    b_vehpesados = models.TextField()  # This field type is a guess.
    b_pare = models.TextField(blank=True, null=True)  # This field type is a guess.
    b_vmax = models.TextField(blank=True, null=True)  # This field type is a guess.
    i_vmax = models.IntegerField(blank=True, null=True)
    b_vmin = models.TextField(blank=True, null=True)  # This field type is a guess.
    i_vmin = models.IntegerField(blank=True, null=True)
    b_zoncarg = models.TextField(blank=True, null=True)  # This field type is a guess.
    b_sensepar = models.TextField(blank=True, null=True)  # This field type is a guess.
    b_resalto = models.TextField(blank=True, null=True)  # This field type is a guess.
    b_depresion = models.TextField(blank=True, null=True)  # This field type is a guess.
    b_reduccalz = models.TextField(blank=True, null=True)  # This field type is a guess.
    b_zonpeat = models.TextField(blank=True, null=True)  # This field type is a guess.
    b_zonescol = models.TextField(blank=True, null=True)  # This field type is a guess.
    b_inifinsepar = models.TextField(blank=True, null=True)  # This field type is a guess.
    b_linbordpav = models.TextField(blank=True, null=True)  # This field type is a guess.
    b_lincarr = models.TextField(blank=True, null=True)  # This field type is a guess.
    b_lincentr = models.TextField(blank=True, null=True)  # This field type is a guess.
    b_demberma = models.TextField(blank=True, null=True)  # This field type is a guess.
    b_reducvel = models.TextField(blank=True, null=True)  # This field type is a guess.
    b_bandalert = models.TextField(blank=True, null=True)  # This field type is a guess.
    b_delinpiso = models.TextField(blank=True, null=True)  # This field type is a guess.
    i_tpdc2p = models.IntegerField(blank=True, null=True)
    i_tpdc2g = models.IntegerField(blank=True, null=True)
    i_tpdc34 = models.IntegerField(blank=True, null=True)
    i_tpdc5 = models.IntegerField(blank=True, null=True)
    i_tpdc5_may = models.IntegerField(blank=True, null=True)
    i_tpda = models.IntegerField(blank=True, null=True)
    i_tpdb = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'i_ope_transito'
        unique_together = (('i_idcons', 'i_idsent'),)




class IValValoracionEconomica(models.Model):
    i_idcons = models.IntegerField(primary_key=True)
    s_idpuente = models.CharField(max_length=25)
    b_infcantsup = Bit1BooleanField()  # This field type is a guess.
    d_supconcr = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    d_suprefact = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    d_suprefpas = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    d_supacero = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    b_infcantsub = Bit1BooleanField()   # This field type is a guess.
    d_subconcr = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    d_subref = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    d_subacero = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    d_subareaaf = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    b_infcantcim = Bit1BooleanField()  # This field type is a guess.
    d_cimconcr = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    d_cimref = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    d_cimmamp = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    b_infcappres = Bit1BooleanField()   # This field type is a guess.
    d_costdis = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    d_costprelim = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    d_costpav = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    d_costpubli = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    d_costestr = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    d_costhidr = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    d_costredes = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    d_costgest = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    d_costadic = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    d_costtotal = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    d_valrepos = models.DecimalField(max_digits=15, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'i_val_valoracion_economica'

class IGenPteIdentifLocalizac(models.Model):
    i_idcons = models.IntegerField(primary_key=True)
    s_idpuente = models.CharField(max_length=25)
    s_nombpuente = models.CharField(max_length=100)
    s_idsipucol = models.CharField(max_length=25, blank=True, null=True)
    s_territ = models.CharField(max_length=50, blank=True, null=True)
    i_tipocarr = models.IntegerField()
    s_idcarr = models.CharField(max_length=10)
    s_nomtramo = models.CharField(max_length=100)
    s_adminvial = models.CharField(max_length=100, blank=True, null=True)
    i_sentpuente = models.IntegerField()
    p_senalidpuen = models.CharField(max_length=500, blank=True, null=True)
    i_obstaculo = models.IntegerField()
    p_obstaculo = models.CharField(max_length=500, blank=True, null=True)
    p_entorno = models.CharField(max_length=500, blank=True, null=True)
    s_carrsalva = models.CharField(max_length=10, blank=True, null=True)
    s_cuerpoagua = models.CharField(max_length=100, blank=True, null=True)
    i_anoconstr = models.IntegerField(blank=True, null=True)
    d_latgra = models.DecimalField(max_digits=10, decimal_places=6)
    d_latmin = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    d_latseg = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    s_lat = models.CharField(max_length=20)
    d_longra = models.DecimalField(max_digits=10, decimal_places=6)
    d_lonmin = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    d_lonseg = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    s_lon = models.CharField(max_length=20)
    s_absi = models.CharField(max_length=10)
    i_absikm = models.IntegerField()
    i_absimm = models.IntegerField()
    s_absf = models.CharField(max_length=10)
    i_absfkm = models.IntegerField()
    i_absfmm = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'i_gen_pte_identif_localizac'

class IGenInformacionGeneral(models.Model):
    i_idcons = models.IntegerField(primary_key=True)
    s_idpuente = models.CharField(max_length=25)
    i_tipolgen = models.IntegerField()
    p_genpuente = models.CharField(max_length=500, blank=True, null=True)
    p_planta = models.CharField(max_length=500, blank=True, null=True)
    p_perfil = models.CharField(max_length=500, blank=True, null=True)
    b_amplmod = models.CharField(max_length=10, blank=True, null=True)
    b_reforz = models.CharField(max_length=10, blank=True, null=True)
    b_pasarela = models.CharField(max_length=10, blank=True, null=True)
    d_wtotal = models.DecimalField(max_digits=10, decimal_places=4)
    d_ltotal = models.DecimalField(max_digits=10, decimal_places=4)
    d_areaplan = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_galsup1 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_galinf1 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_galhor1 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_galsup2 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_galinf2 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_galhor2 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    i_numluces = models.IntegerField()
    i_numapoyint = models.IntegerField()
    i_numjuntas = models.IntegerField()
    i_numcalz = models.IntegerField(blank=True, null=True)
    i_numcarr1 = models.IntegerField(blank=True, null=True)
    i_numcarr2 = models.IntegerField(blank=True, null=True)
    d_wcarr1 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_wcarr2 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_wcalz1 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_wcalz2 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_wberma1 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_wberma2 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    p_gencalzada = models.CharField(max_length=500, blank=True, null=True)
    d_numcalzbajo = models.IntegerField(blank=True, null=True)
    d_numcarrbajo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'i_gen_informacion_general'

class IExgEntorno(models.Model):
    i_idcons = models.IntegerField(primary_key=True)
    s_idpuente = models.CharField(max_length=25)
    d_tefpuente = models.DecimalField(max_digits=10, decimal_places=4)
    d_tarriba = models.DecimalField(max_digits=10, decimal_places=4)
    d_tabajo = models.DecimalField(max_digits=10, decimal_places=4)
    p_caucearriba = models.CharField(max_length=500, blank=True, null=True)
    p_cauceagabajo = models.CharField(max_length=500, blank=True, null=True)
    i_afluent = models.IntegerField()
    d_disaflar = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_disaflab = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    i_tipmatcanal = models.IntegerField()
    b_unimatcanal = models.TextField(blank=True, null=True)  # This field type is a guess.
    p_matcanal = models.CharField(max_length=500, blank=True, null=True)
    i_tipmatizq = models.IntegerField()
    b_unimatizq = models.TextField(blank=True, null=True)  # This field type is a guess.
    p_matizq = models.CharField(max_length=500, blank=True, null=True)
    i_tipmatder = models.IntegerField()
    b_unimatder = models.TextField(blank=True, null=True)  # This field type is a guess.
    p_matder = models.CharField(max_length=500, blank=True, null=True)
    i_tipmatbarsed = models.IntegerField(blank=True, null=True)
    b_unimatbarsed = models.TextField(blank=True, null=True)  # This field type is a guess.
    p_matbarsed = models.CharField(max_length=500, blank=True, null=True)
    i_estrhidr = models.IntegerField()
    i_estreros = models.IntegerField()
    i_estrinund = models.IntegerField()
    i_estrconagua = models.IntegerField()
    i_ubictalud = models.IntegerField()
    p_taludpuente = models.CharField(max_length=500, blank=True, null=True)
    i_numaptalud = models.IntegerField()
    p_aptalud = models.CharField(max_length=500, blank=True, null=True)
    i_tipmatlad = models.IntegerField()
    i_pendtalud = models.IntegerField()
    i_htalud = models.IntegerField()
    i_vegtalud = models.IntegerField()
    b_estrtalud = models.TextField()  # This field type is a guess.
    i_tipestrtalud = models.IntegerField()
    d_hesttalud = models.DecimalField(max_digits=10, decimal_places=4)
    d_lesttalud = models.DecimalField(max_digits=10, decimal_places=4)
    i_numterraz = models.IntegerField(blank=True, null=True)
    p_estrtalud = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'i_exg_entorno'



class IEstElementoServicio(models.Model):
    i_idcons = models.IntegerField(primary_key=True)
    s_idpuente = models.CharField(max_length=25)
    i_matsuprod = models.IntegerField()
    d_wsuprod = models.DecimalField(max_digits=10, decimal_places=4)
    d_lsuprod = models.DecimalField(max_digits=10, decimal_places=4)
    d_tsuprod = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    b_border = models.CharField(max_length=100)
    d_wborder = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_lborder = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_hborder = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    b_borizq = models.CharField(max_length=100)
    d_wborizq = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_lborizq = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_hborizq = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    b_barder = models.CharField(max_length=100)
    i_confbarder = models.IntegerField(blank=True, null=True)
    d_bbarder = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_lbarder = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_hbarder = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    p_barder = models.CharField(max_length=500, blank=True, null=True)
    b_barizq = models.CharField(max_length=100)
    i_confbarizq = models.IntegerField(blank=True, null=True)
    d_bbarizq = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_lbarizq = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_hbarizq = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    p_barizq = models.CharField(max_length=500, blank=True, null=True)
    b_andder = models.CharField(max_length=100)
    i_matandder = models.IntegerField(blank=True, null=True)
    d_wandder = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_landder = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_handder = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    b_andizq = models.CharField(max_length=100)
    i_matandizq = models.IntegerField(blank=True, null=True)
    d_wandizq = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_landizq = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_handizq = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    b_cerram = models.CharField(max_length=100, blank=True, null=True)
    b_separ = models.CharField(max_length=100, blank=True, null=True)
    i_matsepar = models.IntegerField(blank=True, null=True)
    d_bsepar = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_lsepar = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    d_hsepar = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    b_dren = models.CharField(max_length=100, blank=True, null=True)
    b_ilum = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'i_est_elemento_servicio'



class IDocDocumentacion(models.Model):
    i_idcons = models.IntegerField(primary_key=True)
    s_idpuente = models.CharField(max_length=25)
    b_regfotos = Bit1BooleanField()  # This field type is a guess.
    s_rutafotos = models.CharField(max_length=500)
    b_esquemas = Bit1BooleanField()  # This field type is a guess.
    s_rutaesquemas = models.CharField(max_length=500)
    b_planplanta = Bit1BooleanField()  # This field type is a guess.
    b_planperfil = Bit1BooleanField()  # This field type is a guess.
    b_plansecc = Bit1BooleanField()  # This field type is a guess.
    b_plandetal = Bit1BooleanField() # This field type is a guess.
    b_planconstr = Bit1BooleanField()  # This field type is a guess.
    b_planasbui = Bit1BooleanField()  # This field type is a guess.
    s_rutaplanos = models.CharField(max_length=500)
    b_contrdis = Bit1BooleanField()  # This field type is a guess.
    b_contrconstr = Bit1BooleanField()  # This field type is a guess.
    b_contrsuper = Bit1BooleanField() # This field type is a guess.
    b_contrmant = Bit1BooleanField() # This field type is a guess.
    b_contrinterv = Bit1BooleanField()  # This field type is a guess.
    s_rutacontratos = models.CharField(max_length=500, blank=True, null=True)
    s_disenador = models.CharField(max_length=200, blank=True, null=True)
    s_constructor = models.CharField(max_length=200, blank=True, null=True)
    s_supervinterv = models.CharField(max_length=200, blank=True, null=True)
    b_memodis = Bit1BooleanField()  # This field type is a guess.
    s_rutamemodis = models.CharField(max_length=500, blank=True, null=True)
    b_memocost = Bit1BooleanField()  # This field type is a guess.
    s_rutamemocost = models.CharField(max_length=500, blank=True, null=True)
    b_memointerv = Bit1BooleanField()  # This field type is a guess.
    s_rutamemoint = models.CharField(max_length=500, blank=True, null=True)
    b_estsuelos = Bit1BooleanField()  # This field type is a guess.
    b_esthidro = Bit1BooleanField()  # This field type is a guess.
    b_estcapcarga = Bit1BooleanField() # This field type is a guess.
    b_estvulsismo = Bit1BooleanField()  # This field type is a guess.
    b_estvulsocav = Bit1BooleanField()  # This field type is a guess.
    s_rutaesting = models.CharField(max_length=500, blank=True, null=True)
    t_fechaconstr = models.DateField(blank=True, null=True)
    t_fechaultinsp = models.DateField(blank=True, null=True)
    b_mantenim = Bit1BooleanField()  # This field type is a guess.
    t_fechaultmant = models.DateField(blank=True, null=True)
    b_interv = Bit1BooleanField() # This field type is a guess.
    t_fechaultinter = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'i_doc_documentacion'
