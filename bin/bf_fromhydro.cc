#include "msu_sampler/master.h"
#include "msu_commonutils/qualifier.h"
#include "msu_boltzmann/msu_boltzmann.h"
#include "msu_commonutils/log.h"
#include <cstring>
using namespace std;

int main(int argc, char *argv[]){
	if (argc != 2) {
		CLog::Info("Usage: msuboltz run_number\n");
		exit(-1);
  }
	CparameterMap parmap;
	CBalanceArrays *barray;
	int run_number=atoi(argv[1]);
	string run_name="pars"+to_string(run_number);
	char message[200];
	int nmerge,nscatter,nannihilate,ncancel_annihilate,nevents,nparts,ievent,ndecay;
	//char logfilename[100];
	//sprintf(logfilename,"msuboltz_log.txt");
	//CLog::Init(logfilename);
	CLog::INTERACTIVE=true;

	string filename="model_output/fixed_parameters.txt";
	parmap.ReadParsFromFile(filename);
	filename="model_output/pars"+to_string(run_number)+"/parameters.txt";
	parmap.ReadParsFromFile(filename);
	CmasterSampler ms(&parmap);
	CpartList *pl=new CpartList(&parmap,ms.reslist);

	ms.partlist=pl;
	//ms.randy->reset(time(NULL));
	//ms.randy->reset(atoi(argv[1]));
	ms.randy->reset(run_number);
	ms.ReadHyper_OSU_2D();

	CMSU_Boltzmann *msuboltz=new CMSU_Boltzmann(run_name,&parmap,ms.reslist);
	msuboltz->InitCascade();
	msuboltz->randy->reset(run_number);
	barray=msuboltz->balancearrays;
	
	nparts=0;
	nevents=parmap.getI("MSU_BOLTZMANN_NEVENTSMAX",10);
	printf("------- nevents=%d\n",nevents);

	CQualifiers qualifiers;
	qualifiers.Read("qualifiers.txt");
	nmerge=nscatter=nannihilate=ncancel_annihilate=ndecay=0;
	msuboltz->ReadMuTInfo();
	msuboltz->nevents=0;
	msuboltz->SetQualifier(qualifiers.qualifier[0]->qualname);
	for(ievent=0;ievent<nevents;ievent++){
		msuboltz->Reset();
		nparts+=ms.MakeEvent();
		msuboltz->InputPartList(pl);
		pl->Clear();
		printf("----------------- WTF\n");
		msuboltz->CheckActions();
		printf("without charges: partmap size=%d\n",int(msuboltz->PartMap.size()));
		printf("action map size=%lu\n",msuboltz->ActionMap.size());
		//if(barray->FROM_UDS){
			//msuboltz->ReadCharges(ievent);
			//msuboltz->GenHadronsFromCharges(); // Generates inter-correlated parts, with bids = (0,1),(2,3)....
			//msuboltz->DeleteCharges();
		//}
		printf("--------------- with charges: partmap size=%d\n",int(msuboltz->PartMap.size()));
		printf("action map size=%lu\n",msuboltz->ActionMap.size());
		msuboltz->PerformAllActions();
		printf("---------------- Actions Performed\n");
		msuboltz->IncrementHadronCount();

		barray->ProcessPartMap();
		if(barray->FROM_UDS)
			barray->ProcessBFPartMap();
		
		nmerge+=msuboltz->nmerge;
		nscatter+=msuboltz->nscatter;
		nannihilate+=msuboltz->nannihilate;
		ncancel_annihilate+=msuboltz->ncancel_annihilate;
		ndecay+=msuboltz->ndecay;
		sprintf(message,"ievent=%lld nparts/event=%g\n",ms.NEVENTS,double(nparts)/double(ms.NEVENTS));
		CLog::Info(message);
	}
	sprintf(message,"ndecay/event=%g, nmerge/event=%g, nscatter/event=%g\n",
		double(ndecay)/double(nevents),double(nmerge)/double(nevents),double(nscatter)/double(nevents));
	CLog::Info(message);
	sprintf(message,"nannihilate=%g, ncancel_annihilate=%g\n",
		double(nannihilate)/double(nevents),double(ncancel_annihilate)/double(nevents));
	CLog::Info(message);
	msuboltz->WriteMuTInfo();
	msuboltz->WriteHadronCount();
	barray->ConstructBFs();
	barray->WriteBFs();
	barray->WriteDenoms();

	CLog::Info("YIPPEE!!!!! We made it all the way through!\n");
	return 0;
}
