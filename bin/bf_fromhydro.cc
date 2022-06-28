#include "msu_sampler/master.h"
#include "msu_commonutils/qualifier.h"
#include "msu_boltzmann/msu_boltzmann.h"
#include "msu_commonutils/log.h"
#include <cstring>
using namespace std;

int main(int argc, char *argv[]){
	if (argc != 4) {
		CLog::Info("Usage: msuboltz run_number ievent0 ieventf\n");
		exit(-1);
  }
  int nevents,ievent0,ieventf,ievent,iqual,NN,Npi,NK;
	int run_number=atoi(argv[1]);
  string run_name="pars"+to_string(run_number);
	CparameterMap parmap;
	char message[200];
	int nmerge,nscatter,nannihilate,ncancel_annihilate,nparts,ndecay;
	//char logfilename[100];
	//sprintf(logfilename,"msuboltz_log.txt");
	//CLog::Init(logfilename);
	CLog::INTERACTIVE=true;
	ievent0=atoi(argv[2]);
	ieventf=atoi(argv[3]);

	string filename="model_output/fixed_parameters.txt";
	parmap.ReadParsFromFile(filename);
	filename="model_output/"+run_name+"/parameters.txt";
	parmap.ReadParsFromFile(filename);
	CmasterSampler ms(&parmap);
	CpartList *pl=new CpartList(&parmap,ms.reslist);

	ms.partlist=pl;
	ms.randy->reset(run_number);
	ms.ReadHyper_OSU_2D();
	CMSU_Boltzmann *msuboltz=new CMSU_Boltzmann(run_name,&parmap,ms.reslist);
	msuboltz->InitCascade();
	CBalanceArrays *barray=msuboltz->balancearrays;
	nevents=ieventf+1-ievent0;
	CQualifiers qualifiers;
	qualifiers.Read("qualifiers.txt");
	for(iqual=0;iqual<qualifiers.nqualifiers;iqual++){
		msuboltz->SetQualifier(qualifiers.qualifier[iqual]->qualname);
		qualifiers.SetPars(msuboltz->parmap,iqual);
		msuboltz->ReadMuTInfo();
		Npi=NK=NN=nparts=0;
		nmerge=nscatter=nannihilate=ncancel_annihilate=ndecay=0;
		for(ievent=ievent0;ievent<=ieventf;ievent++){
			msuboltz->Reset();
			msuboltz->randy->reset(ievent);
			nparts+=ms.MakeEvent();
			msuboltz->InputPartList(pl);
			Npi+=pl->CountResonances(211)+pl->CountResonances(-221)+pl->CountResonances(111);
			NK+=pl->CountResonances(321)+pl->CountResonances(-321)+pl->CountResonances(311)+pl->CountResonances(-311);
			NN+=pl->CountResonances(2212)+pl->CountResonances(-2212)+pl->CountResonances(2112)+pl->CountResonances(-2112);
			pl->Clear();
			if(msuboltz->BFCALC){
				if(barray->FROM_UDS){
					msuboltz->ReadCharges(ievent);
					msuboltz->GenHadronsFromCharges();
				// Generates inter-correlated parts, with bids = (0,1),(2,3)....
					msuboltz->DeleteCharges();
				}
			}
			msuboltz->PerformAllActions();
			msuboltz->IncrementHadronCount();

			nmerge+=msuboltz->nmerge;
			nscatter+=msuboltz->nscatter;
			nannihilate+=msuboltz->nannihilate;
			ncancel_annihilate+=msuboltz->ncancel_annihilate;
			ndecay+=msuboltz->ndecay;
			sprintf(message,"ievent=%lld nparts/event=%g\n",ms.NEVENTS,double(nparts)/double(ms.NEVENTS));
			CLog::Info(message);

			if(msuboltz->BFCALC){
				barray->ProcessPartMap();
				if(barray->FROM_UDS)
					barray->ProcessBFPartMap();
			}
		}
		sprintf(message,"Npi=%d, NK=%d, NN=%d, NN/Npi=%g\n",Npi,NK,NN,double(NN)/double(Npi));
		CLog::Info(message);
		sprintf(message,"ndecay/event=%g, nmerge/event=%g, nscatter/event=%g\n",
			double(ndecay)/double(nevents),double(nmerge)/double(nevents),double(nscatter)/double(nevents));
		CLog::Info(message);
		sprintf(message,"nannihilate=%g, ncancel_annihilate=%g\n",
			double(nannihilate)/double(nevents),double(ncancel_annihilate)/double(nevents));
		CLog::Info(message);

		if(msuboltz->BFCALC){
			barray->ConstructBFs();
			barray->WriteBFs();

			barray->WriteDenoms();
			barray->WriteGammaP();
		}
	//msuboltz->WriteMuTInfo();
		msuboltz->WriteHadronCount();
	}

	CLog::Info("YIPPEE!!!!! We made it all the way through!\n");
	return 0;
}
