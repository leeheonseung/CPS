from iconservice import *
from .checkers import *

# ================================================
#  Consts
# ================================================
# TAG
TAG = 'CPS_Score'
# ICX Multiplier
_MULTIPLIER = 10 ** 18
# 2/3 Vote
_MAJORITY = 0.666
# Period Interval Time
_BLOCKS_COUNT = 300
# SYSTEM SCORE Address
ZERO_SCORE_ADDRESS = Address.from_string('cx0000000000000000000000000000000000000000')

# BURN COIN ADDRESS
ZERO_WALLET_ADDRESS = Address.from_string('hx0000000000000000000000000000000000000000')


class InterfaceSystemScore(InterfaceScore):
    @interface
    def getPReps(self, start_ranking: int, end_ranking: int) -> list: pass

    @interface
    def getMainPReps(self) -> dict: pass

    @interface
    def getPRepTerm(self) -> dict: pass


class CPF_TREASURY_INTERFACE(InterfaceScore):
    @interface
    def transfer_proposal_fund_to_cps_treasury(self, _ipfs_key: str, _total_installment_count: int, _title: str,
                                               _sponsor_address: str, _contributor_address: str,
                                               _total_budget: int = 0) -> None:
        pass

    @interface
    def update_proposal_fund(self, _ipfs_key: str, _total_added_budget: int = 0,
                             _total_added_installment_count: int = 0) -> None:
        pass

    @interface
    def return_fund_amount(self) -> None:
        pass


class CPS_TREASURY_INTERFACE(InterfaceScore):
    @interface
    def send_installment_to_contributor(self, _ipfs_key: str) -> None:
        pass

    @interface
    def send_reward_to_sponsor(self, _ipfs_key: str) -> None:
        pass

    @interface
    def disqualify_project(self, _ipfs_key: str) -> None:
        pass

    @interface
    def get_contributor_projected_fund(self, _wallet_address: str) -> dict:
        pass

    @interface
    def get_sponsor_projected_fund(self, _wallet_address: str) -> dict:
        pass


class CPS_Score(IconScoreBase):
    PERIOD_TYPE = ["Application Period", "Voting Period"]

    _STATUS = "_status"
    _SPONSOR_PENDING = '_sponsor_pending'
    _PENDING = '_pending'
    _ACTIVE = '_active'
    _PAUSED = "_paused"
    _DISQUALIFIED = "_disqualified"
    _REJECTED = "_rejected"
    _COMPLETED = "_completed"
    STATUS_TYPE = [_SPONSOR_PENDING, _PENDING, _ACTIVE, _PAUSED, _DISQUALIFIED, _REJECTED, _COMPLETED]
    _WAITING = "_waiting"
    _APPROVED = "_approved"
    _PROGRESS_REPORT_REJECTED = "progress_report_rejected"
    PROGRESS_REPORT_STATUS_TYPE = [_APPROVED, _WAITING, _REJECTED]

    _MAIN_PREPS = "_main_preps"
    _ALL_PREPS = "_all_preps"
    _UNREGISTERED_PREPS = "unregistered_preps"
    _PREPS_DENYLIST = "preps_denylist"
    _INACTIVE_PREPS = "inactive_preps"
    _DENYLIST1 = "denylist1"
    _DENYLIST2 = "denylist2"
    _DENYLIST3 = "denylist3"
    _DEPOSIT_STATUS = "deposit_status"

    _PROJECT_TITLE = "_proposal_title"
    _BUDGET = "budget"
    _TOTALVOTES = "totalStaked"
    _TIMESTAMP = '_timestamp'
    _SPONSOR_ADDRESS = "_sponsor_address"
    _CONTRIBUTOR_ADDRESS = "_contributor_address"
    _TX_HASH = "_tx_hash"
    _IPFS_HASH = "_ipfs_hash"
    _IPFS_KEY = "_ipfs_key"
    _PERIOD_COUNT = "_period_count"
    _PERCENTAGE_COMPLETED = "percentage_completed"

    _PROJECT_REPORT_TITLE = "_project_report_title"
    _ADJUSTMENT_AMOUNT = "_adjustment_amount"
    _AMOUNT = "_total_amount"
    _REMAINING_TIME = "remaining_time"
    _BUDGET_APPROVALS_KEY_LIST = "budget_approvals_key_list"
    _BUDGET_APPROVALS_VOTERS = "budget_approvals_voters"
    _BUDGET_VOTES = "_budget_votes"

    _INITIAL_BLOCK = "_initial_block"
    _PERIOD_DETAILS = "_period_details"
    _PERIOD_NAME = "_period_name"
    _APPLICATION_PERIOD = "application_period"
    _VOTING_PERIOD = "voting_period"
    _LASTBLOCK = "last_block"
    _CURRENTBLOCK = "_current_block"
    _NEXTBLOCK = "_next_block"
    _ADMINS = "_admins"

    _CONTRIBUTORS = "_contributors"
    _SPONSORS = "_sponsors"
    _VOTE_DETAILS = "vote_details"
    _VOTERS_DETAILS = "voters_details"
    _VOTERS_LIST = "voters_list"
    _REPORTS_VOTE_DETAILS = "reports_vote_details"
    _REPORTS_VOTERS_DETAILS = "reports_voters_details"
    _REPORTS_VOTERS_LIST = "reports_voters_list"
    _PROPOSALS_BY_HASH = "_proposals_by_hash"
    _PROPOSALS_DETAILS = "_proposal_details"
    _PROPOSALS_STATUS = "_proposal_status"
    _PROPOSALS_KEYS = "_proposal_keys"
    _PROPOSALS_KEY_LIST = '_proposals_key_list'
    _PROGRESS_KEY_LIST = '_progress_key_list'
    _PROGRESS_REPORT_DETAILS = "_progress_report_details"
    _PROGRESS_REPORT_KEYS = "_progress_report_keys"
    _BUDGET_VOTERS_LIST = "budget_voters_list"
    _REPORT_KEY = "_report_key"
    _SPONSOR_DEPOSIT = "sponsor_deposit"
    _DEPOSIT_AMOUNT = "deposit_amount"
    _PENALTY_AMOUNT1 = "penalty_amount1"
    _PENALTY_AMOUNT2 = "penalty_amount2"
    _PENALTY_AMOUNT3 = "penalty_amount3"

    _VOTING_PROPOSALS = "voting_proposals"
    _VOTING_PROGRESS_REPORTS = "voting_progress_reports"
    _ACTIVE_PROPOSALS = "active_proposals"

    _VOTERS = "voters"
    _VOTE = "vote"
    _STAKE_WEIGHT = "stake_weight"
    _ADDRESS = "address"

    _TOTAL_STAKE = "total_stake"

    _PREP_DETAILS = "_prep_details"
    _CPS_TREASURY_SCORE = "_cps_treasury_score"
    _CPF_SCORE = "_cpf_score"

    @eventlog(indexed=3)
    def ProposalSubmitted(self, _sender_address: Address, _score_address: Address, note: str):
        pass

    @eventlog(indexed=3)
    def TokenBurn(self, _sender_address: Address, _score_address: Address, note: str):
        pass

    @eventlog(indexed=3)
    def ProgressReportSubmitted(self, _sender_address: Address, _score_address: Address, _project_title: str):
        pass

    @eventlog(indexed=3)
    def SponsorBondReceived(self, _sender_address: Address, _score_address: Address, _notes: str):
        pass

    @eventlog(indexed=2)
    def PRepPenalty(self, _prep_address: Address, _notes: str):
        pass

    @eventlog(indexed=2)
    def UnRegisterPRep(self, _sender_address: Address, _notes: str):
        pass

    @eventlog(indexed=3)
    def SponsorBondReturned(self, _score_address: Address, _sender_address: Address, _notes: str):
        pass

    def __init__(self, db: IconScoreDatabase) -> None:
        super().__init__(db)

        self._system_score = self.create_interface_score(ZERO_SCORE_ADDRESS, InterfaceSystemScore)

        self.initial_block = VarDB(self._INITIAL_BLOCK, db, value_type=int)

        self.cps_treasury_score = VarDB(self._CPS_TREASURY_SCORE, db, value_type=Address)
        self.cpf_score = VarDB(self._CPF_SCORE, db, value_type=Address)

        self.period_name = VarDB(self._PERIOD_NAME, db, value_type=str)
        self.next_block = VarDB(self._NEXTBLOCK, db, value_type=int)

        self.admins = ArrayDB(self._ADMINS, db, value_type=Address)
        self.contributors = ArrayDB(self._CONTRIBUTORS, db, value_type=Address)
        self.sponsors = ArrayDB(self._SPONSORS, db, value_type=Address)
        self.voters = ArrayDB(self._VOTERS, db, value_type=Address)

        self.voting_proposals = ArrayDB(self._VOTING_PROPOSALS, db, value_type=str)
        self.voting_progress_reports = ArrayDB(self._VOTING_PROGRESS_REPORTS, db, value_type=str)
        self.active_proposals = ArrayDB(self._ACTIVE_PROPOSALS, db, value_type=str)

        self._sponsor_pending = ArrayDB(self._SPONSOR_PENDING, db, value_type=str)
        self._pending = ArrayDB(self._PENDING, db, value_type=str)
        self._active = ArrayDB(self._ACTIVE, db, value_type=str)
        self._paused = ArrayDB(self._PAUSED, db, value_type=str)
        self._completed = ArrayDB(self._COMPLETED, db, value_type=str)
        self._rejected = ArrayDB(self._REJECTED, db, value_type=str)
        self._disqualified = ArrayDB(self._DISQUALIFIED, db, value_type=str)
        self._waiting = ArrayDB(self._WAITING, db, value_type=str)
        self._approved = ArrayDB(self._APPROVED, db, value_type=str)
        self._progress_rejected = ArrayDB(self._PROGRESS_REPORT_REJECTED, db, value_type=str)

        self.proposals_status = {self._SPONSOR_PENDING: self._sponsor_pending,
                                 self._PENDING: self._pending,
                                 self._ACTIVE: self._active,
                                 self._PAUSED: self._paused,
                                 self._COMPLETED: self._completed,
                                 self._REJECTED: self._rejected,
                                 self._DISQUALIFIED: self._disqualified}

        self.progress_report_status = {self._WAITING: self._waiting,
                                       self._APPROVED: self._approved,
                                       self._REJECTED: self._progress_rejected}

        self._main_preps = ArrayDB(self._MAIN_PREPS, db, value_type=str)
        self._all_preps = ArrayDB(self._ALL_PREPS, db, value_type=str)
        self.unregistered_preps = ArrayDB(self._UNREGISTERED_PREPS, db, value_type=str)
        self.inactive_preps = ArrayDB(self._INACTIVE_PREPS, db, value_type=str)

        self.penalty_amount1 = VarDB(self._PENALTY_AMOUNT1, db, value_type=int)
        self.penalty_amount2 = VarDB(self._PENALTY_AMOUNT2, db, value_type=int)
        self.penalty_amount3 = VarDB(self._PENALTY_AMOUNT3, db, value_type=int)

        self.denylist = ArrayDB(self._PREPS_DENYLIST, db, value_type=str)
        self.denylist1 = ArrayDB(self._DENYLIST1, db, value_type=str)
        self.denylist2 = ArrayDB(self._DENYLIST2, db, value_type=str)
        self.denylist3 = ArrayDB(self._DENYLIST3, db, value_type=str)
        self.preps_denylist = {self._DENYLIST1: self.denylist1,
                               self._DENYLIST2: self.denylist2,
                               self._DENYLIST3: self.denylist3}

        self._proposals_key_list = ArrayDB(self._PROPOSALS_KEY_LIST, db, value_type=str)
        self._progress_key_list = ArrayDB(self._PROGRESS_KEY_LIST, db, value_type=str)
        self.budget_approvals_key_list = ArrayDB(self._BUDGET_APPROVALS_KEY_LIST, db, value_type=str)
        self.proposals_txHash = ArrayDB(self._PROPOSALS_BY_HASH, db, value_type=str)

        self.prep_details = DictDB(self._PREP_DETAILS, db, value_type=str, depth=2)
        self.vote_details = DictDB(self._VOTE_DETAILS, db, value_type=int, depth=2)
        self.voters_list = DictDB(self._VOTERS_LIST, db, value_type=str, depth=2)
        self.voters_details = DictDB(self._VOTERS_DETAILS, db, value_type=str, depth=3)

        self.report_voters_details = DictDB(self._REPORTS_VOTERS_DETAILS, db, value_type=int, depth=2)
        self.report_voters_list = DictDB(self._REPORTS_VOTERS_LIST, db, value_type=str, depth=2)
        self.report_vote_details = DictDB(self._REPORTS_VOTE_DETAILS, db, value_type=str, depth=3)

        self.budget_votes = DictDB(self._BUDGET_VOTES, db, value_type=int, depth=2)
        self.budget_voters_list = DictDB(self._BUDGET_VOTERS_LIST, db, value_type=str, depth=2)
        self.budget_approvals_voters = DictDB(self._BUDGET_APPROVALS_VOTERS, db, value_type=str, depth=3)

        self.sponsor_deposit = DictDB(self._SPONSOR_DEPOSIT, db, value_type=str, depth=2)
        self.progress_report_keys = DictDB(self._PROGRESS_REPORT_KEYS, db, value_type=str)
        self.proposal_details = DictDB(self._PROPOSALS_DETAILS, db, value_type=str, depth=2)
        self.progress_report_details = DictDB(self._PROGRESS_REPORT_DETAILS, db, value_type=str, depth=3)

    def on_install(self) -> None:
        super().on_install()

    def on_update(self) -> None:
        super().on_update()

    @external(readonly=True)
    def name(self) -> str:
        return "CPS_SCORE"

    def _prep_only(self) -> None:
        """
        Check for confirming if the sender is the owner of contract
        :return:
        """
        if str(self.msg.sender) not in self._main_preps:
            revert("Only a Top 100 P-Rep can call this method")

    @payable
    def fallback(self):
        revert('Payments can only be sent using _submitProposal method.')

    def check_period(self):
        if self.next_block.get() < self.block_height:
            revert("Update of period required.")

    @only_owner
    @external
    def set_cps_treasury_score(self, _score: Address) -> None:
        """
        Sets the cps treasury score address. Only owner can set the address.
        :param _score: Address of the cps treasury score address
        :type _score: :class:`iconservice.base.address.Address`
        :return:
        """
        if _score.is_contract:
            self.cps_treasury_score.set(_score)

    @external(readonly=True)
    def get_cps_treasury_score(self) -> Address:
        """
        Returns the cps treasury score address
        :return: cps treasury score address
        :rtype: :class:`iconservice.base.address.Address`
        """
        return self.cps_treasury_score.get()

    @only_owner
    @external
    def set_cpf_score(self, _score: Address) -> None:
        """
        Sets the cps treasury score address. Only owner can set the address.
        :param _score: Address of the cps treasury score address
        :type _score: :class:`iconservice.base.address.Address`
        :return:
        """
        if _score.is_contract:
            self.cpf_score.set(_score)

    @external(readonly=True)
    def get_cpf_score(self) -> Address:
        """
        Returns the cps treasury score address
        :return: cps treasury score address
        :rtype: :class:`iconservice.base.address.Address`
        """
        return self.cpf_score.get()

    def set_PReps(self) -> None:
        """
        Set the list of P-Reps' address for the period
        :return:
        """
        # _prep_list = self.get_preps_address()
        #
        # for preps in self._all_preps:
        #     if str(preps) in _prep_list:
        #         self._main_preps.put(preps)

        for prep in range(0, len(self._main_preps)):
            self._main_preps.pop()

        for x in self._all_preps:
            if x not in self.denylist:
                if x not in self.unregistered_preps:
                    self._main_preps.put(x)

    @only_owner
    @external
    def add_PReps(self, _name: str, _address: str, _delegated: int = 0) -> None:
        """
        add P-Rep address with details
        :return:
        """
        if _address not in self._all_preps:
            self._all_preps.put(_address)

            self.prep_details[_address]["name"] = _name
            self.prep_details[_address]["delegated"] = str(_delegated)

    def get_preps_address(self) -> list:
        """
        Returns the all Main P-Reps and SubP-Reps details for the term
        :return: all Main P-Reps and SubP-Reps full details
        """
        _preps_list = []
        # _all_preps = self._system_score.getPRepTerm()['preps']
        # for _prep in range(0, len(_all_preps)):
        #     _preps_list.append(_all_preps[_prep]['address'])

        for prep in self._main_preps:
            _preps_list.append(prep)

        return _preps_list

    @external(readonly=True)
    def get_PReps(self) -> list:
        """
        Returns the all P-Reps who can be active in this period
        :return: P-Rep address list
        """
        _preps = []
        for prep in self._main_preps:
            _preps.append({"name": self.prep_details[prep]["name"],
                           "address": prep,
                           "delegated": int(self.prep_details[prep]["delegated"])})
        return _preps

    @external(readonly=True)
    def login_prep(self, _address: str) -> dict:
        """
        Checks the logged in user is P-Rep or not.
        :return : dict of logged in information

        """

        _login_dict = {}

        if _address in self._all_preps:
            _login_dict["isPRep"] = True

            if _address in self.unregistered_preps:
                _login_dict["isRegistered"] = False
                _login_dict["payPenalty"] = False

            if _address in self.denylist:
                _login_dict["isRegistered"] = False
                _login_dict["payPenalty"] = True

                if _address in self.denylist1:
                    _penalty_amount = self.penalty_amount1.get()
                elif _address in self.denylist2:
                    _penalty_amount = self.penalty_amount2.get()
                else:
                    _penalty_amount = self.penalty_amount3.get()

                _login_dict["penaltyAmount"] = _penalty_amount

            if _address in self._main_preps:
                _login_dict["isRegistered"] = True
                _login_dict["payPenalty"] = False

        else:
            _login_dict["isPRep"] = False
            _login_dict["isRegistered"] = False
            _login_dict["payPenalty"] = False

        return _login_dict

    def get_stake(self, _address: str) -> int:
        """
        get the total stake weight of given address
        :param _address : P-Rep Address
        :return : total delegated amount (loop)
        """

        # _all_preps = self._system_score.getPRepTerm()['preps']
        # for _prep in range(0, len(_all_preps)):
        #     if _prep == _address:
        #         return int(_all_preps[_prep]['delegated'])

        for _prep in self._all_preps:
            if _prep == _address:
                return int(self.prep_details[_prep]['delegated'])

    @only_owner
    @external
    def add_admin(self, _address: Address):
        """
        Adds the admins
        :return :
        """
        _admin_list = self.admins

        if _address not in self.admins:
            self.admins.put(_address)

    @external
    def unregister_prep(self) -> None:
        """
        Unregister a registered P-Rep from CPS.
        :return:
        """

        _address = str(self.msg.sender)

        if _address not in self._main_preps:
            revert("P-Rep is not registered yet.")

        _data_out = self._main_preps.pop()
        if _data_out != _address:
            for prep in range(0, len(self._main_preps)):
                if self._main_preps[prep] == _address:
                    self._main_preps[prep] = _data_out

        self.unregistered_preps.put(_address)
        self.UnRegisterPRep(self.msg.sender, f'{_address} has ben unregistered successfully.')

    @external
    def register_prep(self) -> None:
        """
        Unregister a registered P-Rep from CPS.
        :return:
        """

        _address = str(self.msg.sender)

        if _address in self._main_preps:
            revert("P-Rep is already registered.")

        if _address in self.denylist:
            revert("You are in denylist. To register, You've to pay Penalty.")

        if _address in self.unregistered_preps:
            _data_out = self._main_preps.pop()
            if _data_out != _address:
                for prep in range(0, len(self._main_preps)):
                    if self._main_preps[prep] == _address:
                        self._main_preps[prep] = _data_out

        self._main_preps.put(_address)

    @only_owner
    @external
    def set_prep_penalty_amount(self, _penalty1: int, _penalty2: int, _penalty3: int) -> None:
        """
        Sets the Penalty amount for the registered P-Rep(s) missing to vote on voting period.
        Only owner can set the address.
        :param _penalty1: First Penalty
        :type _penalty1: int
        :param _penalty2: Second Penalty
        :type _penalty2: int
        :param _penalty3: Final Penalty
        :type _penalty3: int
        :return:
        """

        self.penalty_amount1.set(_penalty1 * _MULTIPLIER)
        self.penalty_amount2.set(_penalty2 * _MULTIPLIER)
        self.penalty_amount3.set(_penalty3 * _MULTIPLIER)

    @payable
    @external
    def pay_prep_penalty(self):
        """
        To remove the address from denylist
        :return:
        """
        _address = str(self.msg.sender)
        if _address not in self.denylist:
            revert(f'{_address} not in denylist.')

        if _address in self.denylist1:
            _penalty_amount = self.penalty_amount1.get()
        elif _address in self.denylist2:
            _penalty_amount = self.penalty_amount2.get()
        else:
            _penalty_amount = self.penalty_amount3.get()

        if self.msg.value != _penalty_amount:
            revert(f'Please pay Penalty amount of {_penalty_amount} ICX to register as a P-Rep.')

        _prep = self.denylist.pop()
        if _prep != _address:
            for prep in range(0, len(self.denylist)):
                if self.denylist[prep] == _address:
                    self.denylist[prep] = _prep

        self._main_preps.put(_address)
        self.PRepPenalty(self.msg.sender,
                         f"{self.msg.value // 10 ** 18} ICX Penalty Received. P-Rep removed from Denylist.")

        self.icx.transfer(ZERO_WALLET_ADDRESS, self.msg.value)
        self.TokenBurn(self.msg.sender, ZERO_WALLET_ADDRESS,
                       f"{self.msg.value // 10 ** 18} ICX Burned from penalty deposit.")

    @external(readonly=True)
    def get_denylist(self) -> dict:
        """
        :return: list of P-Rep denylist
        """
        denylist_preps = []
        denied_preps = {}
        for x in self.denylist1:
            denylist_preps.append(x)

        denied_preps['first_penalty'] = denylist_preps
        denylist_preps = []
        for y in self.denylist2:
            denylist_preps.append(y)

        denied_preps['second_penalty'] = denylist_preps
        denylist_preps = []
        for z in self.denylist3:
            denylist_preps.append(z)

        denied_preps['final_penalty'] = denylist_preps

        return denied_preps

    @only_owner
    @external
    def set_initialBlock(self, _block_height: int) -> None:
        """
        To set the initial block of application period to start (once only)
        :_block_height : the initial block to be set
        :return:
        """

        self.set_PReps()
        if _block_height < self.block_height:
            _block_height = self.block_height
        self.initial_block.set(_block_height)

        self.next_block.set(self.initial_block.get() + _BLOCKS_COUNT)
        self.period_name.set("Application Period")

    @external(readonly=True)
    def get_period_status(self) -> dict:
        """
        To get the period status
        :return: dict of status
        """

        _remaining_blocks = self.next_block.get() - self.block_height
        if _remaining_blocks < 0:
            _remaining_blocks = 0
        period_dict = {self._CURRENTBLOCK: self.block_height,
                       self._NEXTBLOCK: self.next_block.get(),
                       self._REMAINING_TIME: _remaining_blocks * 2,
                       self._PERIOD_NAME: self.period_name.get(),
                       "period_span": _BLOCKS_COUNT * 2}

        return period_dict

    @application_period
    @external
    @payable
    def submit_proposal(self, _title: str, _total_budget: int, sponsor_address: str, _ipfs_hash: str, _ipfs_key: str,
                        _ipfs_link: str, project_period: int) -> None:
        """
        User to Submit a proposal
        :param _title : Project Title
        :type _title : str
        :param _total_budget : Total Proposed Budget for the project
        :type _total_budget : int
        :param sponsor_address : Selected P-Rep address to 10% Sponsor bond for the project.
        :type sponsor_address : str
        :param _ipfs_hash : IPFS Hash for the submission
        :type _ipfs_hash : str
        :param _ipfs_key: IPFS Key for the Project
        :type _ipfs_key : str
        :param _ipfs_link : Link for retrieving the details submitted
        :type _ipfs_link : str
        :param project_period: total time period for this project
        :type project_period : int
        """
        _contributor_address = self.msg.sender
        if _contributor_address.is_contract:
            revert("Contract Address not supported.")

        if sponsor_address not in self._main_preps:
            revert("Sponsor P-Rep not a Top 100 P-Rep.")

        if self.msg.value != 50 * _MULTIPLIER:
            revert("Deposit 50 ICX to submit a proposal.")

        _tx_hash = str(bytes.hex(self.tx.hash))

        if _ipfs_key not in self._proposals_key_list:
            self.proposals_txHash.put(_tx_hash)
            self._proposals_key_list.put(_ipfs_key)

            self.proposal_details[_ipfs_key][self._PROJECT_TITLE] = _title
            self.proposal_details[_ipfs_key][self._CONTRIBUTOR_ADDRESS] = str(_contributor_address)
            self.proposal_details[_ipfs_key][self._SPONSOR_ADDRESS] = sponsor_address
            self.proposal_details[_ipfs_key][self._BUDGET] = str(_total_budget)
            self.proposal_details[_ipfs_key][self._TIMESTAMP] = str(self.now())
            self.proposal_details[_ipfs_key][self._TX_HASH] = _tx_hash
            self.proposal_details[_ipfs_key][self._IPFS_HASH] = _ipfs_hash
            self.proposal_details[_ipfs_key][self._PERIOD_COUNT] = str(project_period)
            self.proposal_details[_ipfs_key][self._STATUS] = self._SPONSOR_PENDING
            self.proposal_details[_ipfs_key][self._PERCENTAGE_COMPLETED] = str(0)

            self._sponsor_pending.put(_ipfs_key)

            if _contributor_address not in self.contributors:
                self.contributors.put(_contributor_address)

            self.ProposalSubmitted(_contributor_address, self.address, "Successfully submitted a Proposal.")
            self.icx.transfer(_contributor_address, self.msg.value)
            self.TokenBurn(_contributor_address, self.address, f"{self.msg.value} ICX transferred to burn.")

        else:
            revert("Hash already Exists")

    @application_period
    @external
    @payable
    def submit_progress_report(self, _ipfs_hash: str, _ipfs_key: str, _report_key: str, _progress_report_title: str,
                               _ipfs_link: str, _budget_adjustment: bool, _completed_percent: int = 0,
                               _additional_month: int = 0, _adjustment_value: int = 0) -> None:
        """
        User to Submit a Progress report for the active proposal
        :param _ipfs_hash : IPFS Hash for the submission
        :type _ipfs_hash : str
        :param _ipfs_key: IPFS Key for the submission
        :type _ipfs_key : str
        :param _report_key: IPFS Key for the progress report submission
        :type _ipfs_key : str
        :param _ipfs_link : Link for retrieving the details submitted
        :type _ipfs_link : str
        :param _progress_report_title : Progress report title
        :type _progress_report_title : str
        :param _budget_adjustment : If there is any budget adjustment application is submitted or not
        :type _budget_adjustment : bool
        :param _additional_month: Additional timeframe(month) for the project
        :type _additional_month: int
        :param _completed_percent: Completed percent on numbers
        :type _completed_percent: int
        :param _adjustment_value : if any budget adjustment value is available
        :type _adjustment_value : int
        """

        _contributor_address = self.msg.sender
        if _contributor_address.is_contract:
            revert("Contract Address not supported.")

        if str(self.msg.sender) != self.proposal_details[_ipfs_key][self._CONTRIBUTOR_ADDRESS]:
            revert("Sorry, You are not the contributor for this project.")

        _timestamp = self.now()
        _tx_hash = str(bytes.hex(self.tx.hash))

        if self.proposal_details[_ipfs_key][self._STATUS] == self._ACTIVE or \
                self.proposal_details[_ipfs_key][self._STATUS] == self._PAUSED:
            self.progress_report_details[_ipfs_key][_report_key][self._STATUS] = self._WAITING
            self.progress_report_details[_ipfs_key][_report_key][self._PROJECT_REPORT_TITLE] = _progress_report_title
            self.progress_report_details[_ipfs_key][_report_key][self._IPFS_HASH] = _ipfs_hash
            self.progress_report_details[_ipfs_key][_report_key][self._TX_HASH] = _tx_hash
            self.progress_report_details[_ipfs_key][_report_key][self._TIMESTAMP] = str(_timestamp)
            self.progress_report_details[_ipfs_key][_report_key][self._PERIOD_COUNT] = str(_additional_month)
            self.progress_report_details[_ipfs_key][_report_key][self._ADJUSTMENT_AMOUNT] = str(_adjustment_value)
            self.proposal_details[_ipfs_key][self._PERCENTAGE_COMPLETED] = str(_completed_percent)

            self._waiting.put(_report_key)

            if _ipfs_key not in self._progress_key_list:
                self._progress_key_list.put(_ipfs_key)

            if self.progress_report_keys[_ipfs_key] == "":
                self.progress_report_keys[_ipfs_key] = _report_key
            else:
                self.progress_report_keys[_ipfs_key] += "," + _report_key

            if _adjustment_value != 0:
                if _report_key not in self.budget_approvals_key_list:
                    self.budget_approvals_key_list.put(_report_key)

            self.ProgressReportSubmitted(_contributor_address, self.address,
                                         f'{_progress_report_title} --> Progress Report Submitted Successfully.')

        else:
            revert("NO ACTIVE/PAUSED Project found for this Key.")

    @application_period
    @external
    @payable
    def approve_sponsor(self, _ipfs_key: str) -> None:
        """
        Selected Sponsor P-Rep to approve the requested proposal for CPS
        :param _ipfs_key : proposal ipfs key
        :type _ipfs_key : str
        """
        _status = self.proposal_details[_ipfs_key][self._STATUS]
        _sponsor = self.proposal_details[_ipfs_key][self._SPONSOR_ADDRESS]

        if str(self.msg.sender) not in self._main_preps:
            revert("Not a P-Rep.")

        if str(self.msg.sender) != _sponsor:
            revert("Not a valid Sponsor.")

        if _status == self._SPONSOR_PENDING:
            _budget = int(self.proposal_details[_ipfs_key][self._BUDGET])

            if self.msg.value != (_budget * _MULTIPLIER) / 10:
                revert("Deposit 10% of the total budget of the project.")

            self.proposal_details[_ipfs_key][self._STATUS] = self._PENDING
            self.proposal_details[_ipfs_key][self._TIMESTAMP] = str(self.now())

            _data_out = self.proposals_status[_status].pop()
            if _data_out != _ipfs_key:
                for p in range(len(self.proposals_status[_status])):
                    if self.proposals_status[_status][p] == _ipfs_key:
                        self.proposals_status[_status][p] = _data_out

            self._pending.put(_ipfs_key)

            self.sponsor_deposit[_ipfs_key][self._SPONSOR_ADDRESS] = str(self.msg.sender)
            self.sponsor_deposit[_ipfs_key][self._DEPOSIT_AMOUNT] = str(self.msg.value)
            self.sponsor_deposit[_ipfs_key][self._TIMESTAMP] = str(self.now())
            self.sponsor_deposit[_ipfs_key][self._CONTRIBUTOR_ADDRESS] = self.proposal_details[_ipfs_key][
                self._CONTRIBUTOR_ADDRESS]
            self.sponsor_deposit[_ipfs_key][self._DEPOSIT_STATUS] = "bond_received"
            self.SponsorBondReceived(self.msg.sender, self.address, "Sponsor Bond Received.")

    @application_period
    @external
    def reject_sponsor(self, _ipfs_key: str) -> None:
        """
        Selected Sponsor P-Rep to reject the requested proposal for CPS
        :param _ipfs_key : proposal ipfs key
        :type _ipfs_key : str
        """
        _status = self.proposal_details[_ipfs_key][self._STATUS]

        if _status == self._SPONSOR_PENDING:
            self.proposal_details[_ipfs_key][self._STATUS] = self._REJECTED
            self.proposal_details[_ipfs_key][self._TIMESTAMP] = str(self.now())

            _data_out = self.proposals_status[_status].pop()
            if _data_out != _ipfs_key:
                for p in range(len(self.proposals_status[_status])):
                    if self.proposals_status[_status][p] == _ipfs_key:
                        self.proposals_status[_status][p] = _data_out

            self._rejected.put(_ipfs_key)

    @external(readonly=True)
    def get_proposals_keys_by_status(self, _status: str) -> list:
        """
        Returns the proposal keys of proposal by status
        :return: list of keys of given status
        :rtype: list
        """
        if _status not in self.STATUS_TYPE:
            revert(f"Not a valid status.")

        _list = []

        for x in self.proposals_status[_status]:
            _list.append(x)

        return _list

    @voting_period
    @external
    def vote_proposal(self, _ipfs_key: str, _vote: str, _vote_reason: str = "") -> None:
        """
        P-Rep(s) voting for a proposal to be approved or not
        :param _ipfs_key : proposal ipfs key
        :type _ipfs_key : str
        :param _vote: vote in [_approve,_reject,_abstain]
        :type _vote : str
        :param _vote_reason : Any specific reason behind the vote
        :type _vote_reason : str
        """
        self._prep_only()

        _status = self.proposal_details[_ipfs_key][self._STATUS]

        _voters_list = str(self.voters_list[_ipfs_key][self._VOTERS])
        _voters = _voters_list.split(",")

        if str(self.msg.sender) in _voters:
            revert("Can't Vote double.")

        if _status == self._PENDING:
            self.vote_details[_ipfs_key][self._TOTALVOTES] += self.get_stake(str(self.msg.sender))

            if self.voters_list[_ipfs_key][self._VOTERS] == "":
                self.voters_list[_ipfs_key][self._VOTERS] = str(self.msg.sender)
            else:
                self.voters_list[_ipfs_key][self._VOTERS] += "," + str(self.msg.sender)

            self.voters_details[_ipfs_key][str(self.msg.sender)][self._VOTE] = _vote
            self.voters_details[_ipfs_key][str(self.msg.sender)][self._STAKE_WEIGHT] = str(self.get_stake(
                str(self.msg.sender)))
            self.voters_details[_ipfs_key][str(self.msg.sender)][self._TIMESTAMP] = str(self.now())

    @voting_period
    @external
    def vote_progress_report(self, _ipfs_key: str, _report_key: str, _vote: str, _budget_adjustment_vote: str = "",
                             _vote_reason: str = "", ) -> None:
        """
        P-Rep(s) voting for a progress report of all active proposals
        :param _ipfs_key : proposal ipfs key
        :type _ipfs_key : str
        :param _report_key : progress report ipfs key
        :type _report_key : str
        :param _vote : voting in [_approve,_reject]
        :type _vote : str
        :param _budget_adjustment_vote: Budget voting Adjustment
        :type _budget_adjustment_vote : str
        :param _vote_reason : Any specific reason behind the vote
        :type _vote_reason : str
        """
        self._prep_only()

        _voters_list = str(self.report_voters_list[_report_key][self._VOTERS])
        _voters = _voters_list.split(",")

        if str(self.msg.sender) in _voters:
            revert("Can't Vote double.")

        if self.progress_report_details[_ipfs_key][_report_key][self._STATUS] == self._WAITING:
            self.report_voters_details[_report_key][self._TOTALVOTES] += self.get_stake(str(self.msg.sender))
            self.report_voters_list[_report_key][self._IPFS_KEY] = _ipfs_key

            if self.report_voters_list[_report_key][self._VOTERS] == "":
                self.report_voters_list[_report_key][self._VOTERS] = str(self.msg.sender)
            else:
                self.report_voters_list[_report_key][self._VOTERS] += "," + str(self.msg.sender)

            self.report_vote_details[_report_key][str(self.msg.sender)][self._VOTE] = _vote
            self.report_vote_details[_report_key][str(self.msg.sender)][self._STAKE_WEIGHT] = str(self.get_stake(
                str(self.msg.sender)))
            self.report_vote_details[_report_key][str(self.msg.sender)][self._TIMESTAMP] = str(self.now())

            if _report_key in self.budget_approvals_key_list:
                self.budget_votes[_report_key][self._TOTALVOTES] += self.get_stake(str(self.msg.sender))
                self.budget_voters_list[_report_key][self._IPFS_KEY] = _ipfs_key
                if self.budget_voters_list[_report_key][self._VOTERS] == "":
                    self.budget_voters_list[_report_key][self._VOTERS] = str(self.msg.sender)
                else:
                    self.budget_voters_list[_report_key][self._VOTERS] += "," + str(self.msg.sender)
                self.budget_approvals_voters[_report_key][str(self.msg.sender)][self._VOTE] = _vote
                self.budget_approvals_voters[_report_key][str(self.msg.sender)][self._STAKE_WEIGHT] = str(
                    self.get_stake(str(self.msg.sender)))
                self.budget_approvals_voters[_report_key][str(self.msg.sender)][self._TIMESTAMP] = str(self.now())

    @external(readonly=True)
    def get_progress_reports(self, _status: str, _address: str = "", _start_index: int = 0,
                             _end_index: int = 20) -> dict:
        """
        Returns all the progress report submitted of given _status
        :param _status : status in ['_approved','_waiting','_rejected']
        :type _status : str
        :param _address : address of logged user
        :type _address : str
        :param _start_index : first index
        :type _start_index : int
        :param _end_index : last index
        :type _end_index : int

        :return : Progress reports with details
        :rtype : dict
        """

        if _status not in self.PROGRESS_REPORT_STATUS_TYPE:
            revert("Not a valid status")

        _progress_report_list = []

        _active_projects = self.get_proposals_keys_by_status(self._ACTIVE)
        _paused_projects = self.get_proposals_keys_by_status(self._PAUSED)
        _progress_keys = _active_projects + _paused_projects
        _progress_report_len = len(_progress_keys)

        if _end_index - _start_index > 50:
            return {-1: "Page length must not be greater than 50."}
        if _start_index < 0:
            _start_index = 0
        count = _progress_report_len

        _range = range(_start_index, count if _end_index > count else _end_index)

        for reports in _range:
            stringKeys = self.progress_report_keys[_progress_keys[reports]]
            _report_key_list = stringKeys.split(',')
            for report in _report_key_list:
                if self.progress_report_details[_progress_keys[reports]][report][self._STATUS] == _status:
                    _vote_result = self.get_progress_report_result(report)
                    _progress_reports_details = {
                        self._STATUS: self.progress_report_details[_progress_keys[reports]][report][self._STATUS],
                        self._PROJECT_TITLE: self.proposal_details[_progress_keys[reports]][self._PROJECT_TITLE],
                        self._PROJECT_REPORT_TITLE: self.progress_report_details[_progress_keys[reports]][report][
                            self._PROJECT_REPORT_TITLE],
                        self._CONTRIBUTOR_ADDRESS: self.proposal_details[_progress_keys[reports]][
                            self._CONTRIBUTOR_ADDRESS],
                        self._TIMESTAMP: self.progress_report_details[_progress_keys[reports]][report][
                            self._TIMESTAMP],
                        self._IPFS_HASH: self.progress_report_details[_progress_keys[reports]][report][
                            self._IPFS_HASH],
                        self._REPORT_KEY: report,
                        self._IPFS_KEY: _progress_keys[reports],
                        "approved_votes": _vote_result['approved_votes'],
                        "rejected_votes": _vote_result['rejected_votes'],
                        "total_votes": _vote_result["total_votes"],
                        "approved_voters": _vote_result["approve_voters"],
                        "rejected_voters": _vote_result["reject_voters"],
                        "total_voters": _vote_result["total_voters"]}
                    _progress_report_list.append(_progress_reports_details)

        progress_report_dict = {"data": _progress_report_list, "count": len(_progress_report_list)}
        return progress_report_dict

    @external(readonly=True)
    def get_progress_reports_by_proposal(self, _ipfs_key: str) -> dict:
        """
        Returns all the progress reports for a specific project
        :param _ipfs_key : project key
        :type _ipfs_key : str

        :return : List of all progress report with status
        :rtype : dict
        """

        _report_keys = self.progress_report_keys[_ipfs_key]
        _reports = _report_keys.split(",")
        _progress_reports = []

        for reports in _reports:
            _vote_result = self.get_progress_report_result(reports)
            _progress_report = {
                self._PROJECT_TITLE: self.proposal_details[_ipfs_key][self._PROJECT_TITLE],
                self._PROJECT_REPORT_TITLE: self.progress_report_details[_ipfs_key][reports][
                    self._PROJECT_REPORT_TITLE],
                self._STATUS: self.progress_report_details[_ipfs_key][reports][self._STATUS],
                self._TIMESTAMP: int(self.progress_report_details[_ipfs_key][reports][self._TIMESTAMP]),
                self._IPFS_KEY: _ipfs_key,
                self._REPORT_KEY: reports,
                self._IPFS_HASH: self.progress_report_details[_ipfs_key][reports][self._IPFS_HASH],
                "approved_votes": _vote_result['approved_votes'],
                "rejected_votes": _vote_result['rejected_votes'],
                "total_votes": _vote_result["total_votes"],
                "approved_voters": _vote_result["approve_voters"],
                "rejected_voters": _vote_result["reject_voters"],
                "total_voters": _vote_result["total_voters"]}
            _progress_reports.append(_progress_report)

        return {"data": _progress_reports}

    @external(readonly=True)
    def get_project_amounts(self) -> dict:
        """
        :return: A dict of amount with the proposal status
        """
        _status_list = ['_pending', '_active', "_paused", "_completed", "_disqualified"]
        _pending_amount = 0
        _active_amount = 0
        _paused_amount = 0
        _completed_amount = 0
        _disqualified_amount = 0
        for status in range(0, len(_status_list)):
            _amount = 0
            for keys in self.get_proposals_keys_by_status(_status_list[status]):
                _amount += int(self.proposal_details[keys][self._BUDGET])

            if status == 0:
                _pending_amount = _amount
            elif status == 1:
                _active_amount = _amount
            elif status == 2:
                _paused_amount = _amount
            elif status == 3:
                _completed_amount = _amount
            elif status == 4:
                _disqualified_amount = _amount

        _amount_dict = {_status_list[0]: {self._AMOUNT: _pending_amount,
                                          "_count": len(self.get_proposals_keys_by_status(_status_list[0]))},
                        _status_list[1]: {self._AMOUNT: _active_amount,
                                          "_count": len(self.get_proposals_keys_by_status(_status_list[1]))},
                        _status_list[2]: {self._AMOUNT: _paused_amount,
                                          "_count": len(self.get_proposals_keys_by_status(_status_list[2]))},
                        _status_list[3]: {self._AMOUNT: _completed_amount,
                                          "_count": len(self.get_proposals_keys_by_status(_status_list[3]))},
                        _status_list[4]: {self._AMOUNT: _disqualified_amount,
                                          "_count": len(self.get_proposals_keys_by_status(_status_list[4]))}}

        return _amount_dict

    @external(readonly=True)
    def get_proposal_detail_by_wallet(self, _wallet_address: str) -> dict:
        """
        Returns a dict of proposals of provided status
        :param _wallet_address : user Signing in
        :type _wallet_address : str


        :return: List of all proposals_details
        """

        if _wallet_address == "":
            return {"Message": "Enter wallet address."}

        _proposals_list = []
        _proposals_keys = self._proposals_key_list

        for _keys in range(0, len(_proposals_keys)):
            if self.proposal_details[_proposals_keys[_keys]][self._CONTRIBUTOR_ADDRESS] == _wallet_address:
                _vote_details = self.get_vote_result(_proposals_keys[_keys])
                _proposals_details = {
                    self._STATUS: self.proposal_details[_proposals_keys[_keys]][self._STATUS],
                    self._PROJECT_TITLE: self.proposal_details[_proposals_keys[_keys]][
                        self._PROJECT_TITLE],
                    self._CONTRIBUTOR_ADDRESS: self.proposal_details[_proposals_keys[_keys]][
                        self._CONTRIBUTOR_ADDRESS],
                    self._BUDGET: int(self.proposal_details[_proposals_keys[_keys]][self._BUDGET]),
                    self._TIMESTAMP: int(self.proposal_details[_proposals_keys[_keys]][self._TIMESTAMP]),
                    self._IPFS_HASH: self.proposal_details[_proposals_keys[_keys]][
                        self._IPFS_HASH],
                    self._IPFS_KEY: _proposals_keys[_keys],
                    "approved_votes": int(_vote_details["approved_votes"]),
                    "rejected_votes": int(_vote_details["rejected_votes"]),
                    "total_votes": int(_vote_details["total_votes"]),
                    self._PERCENTAGE_COMPLETED: int(self.proposal_details[_proposals_keys[_keys]][
                                                        self._PERCENTAGE_COMPLETED])}
                _proposals_list.append(_proposals_details)

        _proposals_dict_list = {"data": _proposals_list, "count": len(_proposals_list)}
        return _proposals_dict_list

    @external(readonly=True)
    def get_proposal_details(self, _status: str, _wallet_address: str = "", _start_index: int = 0,
                             _end_index: int = 20) -> dict:
        """
        Returns a dict of proposals of provided status
        :param _status : status in ['_active','_pending','_rejected','_completed','_disqualified','_sponsor_pending']
        :type _status : str
        :param _wallet_address : user Signing in
        :type _wallet_address : str
        :param _start_index : first index
        :type _start_index : int
        :param _end_index : last index
        :type _end_index : int


        :return: List of all proposals_details
        """

        if _status not in self.STATUS_TYPE:
            return {-1: "Not a valid status."}

        _proposals_list = []
        _proposals_keys = self.get_proposals_keys_by_status(_status)

        if _end_index - _start_index > 50:
            return {-1: "Page length must not be greater than 50."}
        if _start_index < 0:
            _start_index = 0
        count = len(_proposals_keys)

        _range = range(_start_index, count if _end_index > count else _end_index)

        for _keys in _range:
            if self.proposal_details[_proposals_keys[_keys]][self._STATUS] == _status:
                _vote_details = self.get_vote_result(_proposals_keys[_keys])
                _proposals_details = {
                    self._STATUS: self.proposal_details[_proposals_keys[_keys]][self._STATUS],
                    self._PROJECT_TITLE: self.proposal_details[_proposals_keys[_keys]][
                        self._PROJECT_TITLE],
                    self._CONTRIBUTOR_ADDRESS: self.proposal_details[_proposals_keys[_keys]][
                        self._CONTRIBUTOR_ADDRESS],
                    self._BUDGET: int(self.proposal_details[_proposals_keys[_keys]][self._BUDGET]),
                    self._TIMESTAMP: int(self.proposal_details[_proposals_keys[_keys]][self._TIMESTAMP]),
                    self._IPFS_HASH: self.proposal_details[_proposals_keys[_keys]][
                        self._IPFS_HASH],
                    self._IPFS_KEY: _proposals_keys[_keys],
                    "approved_votes": int(_vote_details["approved_votes"]),
                    "rejected_votes": int(_vote_details["rejected_votes"]),
                    "total_votes": int(_vote_details["total_votes"]),
                    self._PERCENTAGE_COMPLETED: int(self.proposal_details[_proposals_keys[_keys]][
                                                        self._PERCENTAGE_COMPLETED])}
                _proposals_list.append(_proposals_details)

        _proposals_dict_list = {"data": _proposals_list, "count": len(_proposals_list)}
        return _proposals_dict_list

    @external(readonly=True)
    def get_active_proposals(self, _wallet_address: str) -> list:
        """
        Returns the list of all all active or paused proposal from that address
        :param _wallet_address : wallet address of the user
        :return: list
        """

        _proposal_titles = []
        _proposals_hashes = self._proposals_key_list

        for proposals in _proposals_hashes:
            if self.proposal_details[proposals][self._STATUS] == self._ACTIVE or \
                    self.proposal_details[proposals][self._STATUS] == self._PAUSED:
                if self.proposal_details[proposals][self._CONTRIBUTOR_ADDRESS] == _wallet_address:
                    _report_keys = self.progress_report_keys[proposals]
                    _reports = _report_keys.split(",")
                    _report = True

                    for report in _reports:
                        if self.progress_report_details[proposals][report][self._STATUS] == self._WAITING:
                            _report = False
                    _proposals_details = {self._PROJECT_TITLE: self.proposal_details[proposals][self._PROJECT_TITLE],
                                          self._IPFS_KEY: proposals,
                                          "new_progress_report": _report}
                    _proposal_titles.append(_proposals_details)

        return _proposal_titles

    @external(readonly=True)
    def get_contributors(self) -> list:
        """
        Returns the list of all contributors address who've submitted proposals to CPS
        :return: List of contributors
        """

        _contributors_list = []

        for address in self.contributors:
            _contributors_list.append(address)

        return _contributors_list

    @external(readonly=True)
    def get_sponsors_list(self) -> list:
        """

        :return: list of sponsors address
        """
        _sponsors_list = []
        for x in self.sponsors:
            _sponsors_list.append(x)

        return _sponsors_list

    @external(readonly=True)
    def get_sponsors_record(self) -> dict:
        """

        :return: dict of P-Reps with their sponsored project counts
        """
        _proposals_keys = []
        _sponsors_list = []

        for a in self.get_proposals_keys_by_status(self._ACTIVE):
            _proposals_keys.append(a)

        for pa in self.get_proposals_keys_by_status(self._PAUSED):
            _proposals_keys.append(pa)

        for c in self.get_proposals_keys_by_status(self._COMPLETED):
            _proposals_keys.append(c)

        for sponsors in _proposals_keys:
            _sponsors_list.append(self.proposal_details[sponsors][self._SPONSOR_ADDRESS])

        sponsors_dict = {i: _sponsors_list.count(i) for i in _sponsors_list}

        return sponsors_dict

    @external(readonly=True)
    def get_sponsors_requests(self, _status: str, _sponsor_address: str, _start_index: int = 0,
                              _end_index: int = 20) -> dict:
        """
        Returns all the sponsored requests for given sponsor address
        :param _status : status in ['_sponsor_pending','_approved','_rejected','_disqualified']
        :type _status : str
        :param _sponsor_address: Sponsor P-Rep address
        :type _sponsor_address: str
        :param _start_index: first index
        :param _end_index: last index

        :return: List of all proposals_details
        :rtype: dict
        """

        _sponsors_request = []
        _proposals_keys = []

        if _status not in ["_approved", self._SPONSOR_PENDING, self._REJECTED, self._DISQUALIFIED]:
            revert("Not valid status.")

        if _status == "_approved":
            for ac in self.get_proposals_keys_by_status(self._ACTIVE):
                _proposals_keys.append(ac)

            for pa in self.get_proposals_keys_by_status(self._PAUSED):
                _proposals_keys.append(pa)

            for com in self.get_proposals_keys_by_status(self._COMPLETED):
                _proposals_keys.append(com)

        else:
            _proposals_keys = self.get_proposals_keys_by_status(_status)

        if _start_index < 0:
            _start_index = 0
        if _end_index - _start_index > 50:
            revert("Page length must not be greater than 50.")

        start = _end_index * _start_index
        count = len(_proposals_keys)

        if start > count:
            return {}

        end = _end_index * (_start_index + 1)
        _range = range(start, count if end > count else end)

        for _keys in _range:
            if self.proposal_details[_proposals_keys[_keys]][self._SPONSOR_ADDRESS] == _sponsor_address:
                if _status == "_approved":
                    _proposals_details = {
                        self._STATUS: self.proposal_details[_proposals_keys[_keys]][self._STATUS],
                        self._PROJECT_TITLE: self.proposal_details[_proposals_keys[_keys]][
                            self._PROJECT_TITLE],
                        self._CONTRIBUTOR_ADDRESS: self.proposal_details[_proposals_keys[_keys]][
                            self._CONTRIBUTOR_ADDRESS],
                        self._BUDGET: int(
                            self.proposal_details[_proposals_keys[_keys]][self._BUDGET]),
                        self._TIMESTAMP: int(
                            self.proposal_details[_proposals_keys[_keys]][self._TIMESTAMP]),
                        self._IPFS_HASH: self.proposal_details[_proposals_keys[_keys]][
                            self._IPFS_HASH],
                        self._IPFS_KEY: _proposals_keys[_keys]}
                    _sponsors_request.append(_proposals_details)

                elif self.proposal_details[_proposals_keys[_keys]][self._STATUS] == _status:
                    _proposals_details = {
                        self._STATUS: self.proposal_details[_proposals_keys[_keys]][self._STATUS],
                        self._PROJECT_TITLE: self.proposal_details[_proposals_keys[_keys]][
                            self._PROJECT_TITLE],
                        self._CONTRIBUTOR_ADDRESS: self.proposal_details[_proposals_keys[_keys]][
                            self._CONTRIBUTOR_ADDRESS],
                        self._BUDGET: int(
                            self.proposal_details[_proposals_keys[_keys]][self._BUDGET]),
                        self._TIMESTAMP: int(
                            self.proposal_details[_proposals_keys[_keys]][self._TIMESTAMP]),
                        self._IPFS_HASH: self.proposal_details[_proposals_keys[_keys]][
                            self._IPFS_HASH],
                        self._IPFS_KEY: _proposals_keys[_keys]}
                    _sponsors_request.append(_proposals_details)

        _sponsors_dict = {"data": _sponsors_request, "count": len(_sponsors_request)}

        return _sponsors_dict

    @external(readonly=True)
    def get_vote_result(self, _ipfs_key: str) -> dict:
        """
        Get vote results by proposal
        :param _ipfs_key : proposal ipfs key
        :type _ipfs_key : str

        :return: Vote status of given _ipfs_key
        :rtype : dict
        """

        _voters_list = self.voters_list[_ipfs_key][self._VOTERS]
        _voters = _voters_list.split(",")
        _vote_status = []

        approved_votes = 0
        rejected_votes = 0
        _approve_voters = 0
        _reject_voters = 0
        if self.vote_details[_ipfs_key][self._TOTALVOTES] is None:
            self.vote_details[_ipfs_key][self._TOTALVOTES] = 0

        if _voters_list == "":
            return {"data": _vote_status, "approve_voters": _approve_voters, "reject_voters": _reject_voters,
                    "total_voters": len(self._main_preps), "approved_votes": approved_votes,
                    "rejected_votes": rejected_votes,
                    "total_votes": int(self.vote_details[_ipfs_key][self._TOTALVOTES])}

        else:
            for voters in _voters:
                _voters = {self._ADDRESS: voters,
                           self._VOTE: self.voters_details[_ipfs_key][voters][self._VOTE],
                           self._TIMESTAMP: int(self.voters_details[_ipfs_key][voters][self._TIMESTAMP])}

                if self.voters_details[_ipfs_key][voters][self._VOTE] == "_approve":
                    approved_votes += int(self.voters_details[_ipfs_key][voters][self._STAKE_WEIGHT])
                    _approve_voters += 1

                if self.voters_details[_ipfs_key][voters][self._VOTE] == "_reject":
                    rejected_votes += int(self.voters_details[_ipfs_key][voters][self._STAKE_WEIGHT])
                    _reject_voters += 1
                _vote_status.append(_voters)

            return {"data": _vote_status, "approve_voters": _approve_voters, "reject_voters": _reject_voters,
                    "total_voters": len(self._main_preps), "approved_votes": approved_votes,
                    "rejected_votes": rejected_votes,
                    "total_votes": int(self.vote_details[_ipfs_key][self._TOTALVOTES])}

    @external(readonly=True)
    def get_progress_report_result(self, _report_key: str) -> dict:
        """
        Get vote results by progress report
        :param _report_key : progress report ipfs key
        :type _report_key : str

        :return: Vote status of given _report_key
        :rtype : dict
        """
        _voters_list = self.report_voters_list[_report_key][self._VOTERS]
        _voters = _voters_list.split(",")
        _vote_status = []

        approved_votes = 0
        rejected_votes = 0
        _approve_voters = 0
        _reject_voters = 0
        if self.report_voters_details[_report_key][self._TOTALVOTES] is None:
            self.report_voters_details[_report_key][self._TOTALVOTES] = 0

        if _voters_list == "":
            return {"data": _vote_status, "approve_voters": _approve_voters, "reject_voters": _reject_voters,
                    "total_voters": len(self._main_preps), "approved_votes": approved_votes,
                    "rejected_votes": rejected_votes,
                    "total_votes": self.report_voters_details[_report_key][self._TOTALVOTES]}

        for voters in _voters:
            _voters = {self._IPFS_KEY: self.report_voters_list[_report_key][self._IPFS_KEY],
                       self._ADDRESS: voters,
                       self._VOTE: self.report_vote_details[_report_key][voters][self._VOTE],
                       self._TIMESTAMP: int(self.report_vote_details[_report_key][voters][self._TIMESTAMP])}

            if self.report_vote_details[_report_key][voters][self._VOTE] == "_approve":
                approved_votes += int(self.report_vote_details[_report_key][voters][self._STAKE_WEIGHT])
                _approve_voters += 1
            if self.report_vote_details[_report_key][voters][self._VOTE] == "_reject":
                rejected_votes += int(self.report_vote_details[_report_key][voters][self._STAKE_WEIGHT])
                _reject_voters += 1
            _vote_status.append(_voters)

        return {"data": _vote_status, "approve_voters": _approve_voters, "reject_voters": _reject_voters,
                "total_voters": len(self._main_preps), "approved_votes": approved_votes,
                "rejected_votes": rejected_votes,
                "total_votes": self.report_voters_details[_report_key][self._TOTALVOTES]}

    @external(readonly=True)
    def get_budget_adjustment_vote_result(self, _report_key: str) -> dict:
        """
        Get budget adjustment vote results
        :param _report_key : progress report ipfs key
        :type _report_key : str

        :return: Vote status of given _report_key
        :rtype : dict
        """
        _voters_list = self.budget_voters_list[_report_key][self._VOTERS]
        _voters = _voters_list.split(",")
        _vote_status = []

        approved_votes = 0
        rejected_votes = 0
        _approve_voters = 0
        _reject_voters = 0

        for voters in _voters:
            _voters = {self._IPFS_KEY: self.budget_voters_list[_report_key][self._IPFS_KEY],
                       self._ADDRESS: voters,
                       self._VOTE: self.budget_approvals_voters[_report_key][str(self.msg.sender)][self._VOTE],
                       self._TIMESTAMP: int(
                           self.budget_approvals_voters[_report_key][str(self.msg.sender)][self._TIMESTAMP])}

            if self.budget_approvals_voters[_report_key][str(self.msg.sender)][self._VOTE] == "yes":
                approved_votes += int(
                    self.budget_approvals_voters[_report_key][str(self.msg.sender)][self._STAKE_WEIGHT])
                _approve_voters += 1
            if self.budget_approvals_voters[_report_key][str(self.msg.sender)][self._VOTE] == "no":
                rejected_votes += int(
                    self.budget_approvals_voters[_report_key][str(self.msg.sender)][self._STAKE_WEIGHT])
                _reject_voters += 1
            _vote_status.append(_voters)

        return {"data": _vote_status, "approve_voters": _approve_voters, "reject_voters": _reject_voters,
                "total_voters": len(self._main_preps), "approved_votes": approved_votes,
                "rejected_votes": rejected_votes,
                "total_votes": self.budget_votes[_report_key][self._TOTALVOTES]}

    @external(readonly=True)
    def get_remaining_project(self, _project_type: str, _wallet_address: str) -> list:
        """
        Returns remaining projects and progress reports to vote on the current voting period
        :param _project_type: "proposal" or "progress_report" which type, remaining votes need to be checked
        :type _project_type: str
        :param _wallet_address: Wallet Address of the P-Rep
        :type _wallet_address: str
        :return: list of details of proposal or progress report what they need to vote on the same voting period
        """
        _remaining_proposals = []
        _remaining_progress_report = []
        if _project_type == "proposal":
            _proposal_keys = self.get_proposals_keys_by_status(self._PENDING)

            for _ipfs_key in _proposal_keys:
                _voters_list = self.voters_list[_ipfs_key][self._VOTERS]
                _voters = _voters_list.split(",")

                if _wallet_address not in _voters:
                    _vote_details = self.get_vote_result(_ipfs_key)
                    _proposals_details = {
                        self._STATUS: self.proposal_details[_ipfs_key][self._STATUS],
                        self._PROJECT_TITLE: self.proposal_details[_ipfs_key][
                            self._PROJECT_TITLE],
                        self._CONTRIBUTOR_ADDRESS: self.proposal_details[_ipfs_key][
                            self._CONTRIBUTOR_ADDRESS],
                        self._BUDGET: int(self.proposal_details[_ipfs_key][self._BUDGET]),
                        self._TIMESTAMP: int(self.proposal_details[_ipfs_key][self._TIMESTAMP]),
                        self._IPFS_HASH: self.proposal_details[_ipfs_key][
                            self._IPFS_HASH],
                        self._IPFS_KEY: _ipfs_key,
                        "approved_votes": int(_vote_details["approved_votes"]),
                        "rejected_votes": int(_vote_details["rejected_votes"]),
                        "total_votes": int(_vote_details["total_votes"]),
                        self._PERCENTAGE_COMPLETED: int(self.proposal_details[_ipfs_key][
                                                            self._PERCENTAGE_COMPLETED])}
                    _remaining_proposals.append(_proposals_details)

            return _remaining_proposals

        if _project_type == "progress_report":
            for _report_key in self._waiting:
                _voters_list = self.report_voters_list[_report_key][self._VOTERS]
                _voters = _voters_list.split(",")

                if _wallet_address not in _voters:
                    _ipfs_key = self.report_voters_list[_report_key][self._IPFS_KEY]
                    _vote_result = self.get_progress_report_result(_report_key)
                    _progress_reports_details = {
                        self._STATUS: self.progress_report_details[_ipfs_key][_report_key][self._STATUS],
                        self._PROJECT_TITLE: self.proposal_details[_ipfs_key][self._PROJECT_TITLE],
                        self._PROJECT_REPORT_TITLE: self.progress_report_details[_ipfs_key][_report_key][
                            self._PROJECT_REPORT_TITLE],
                        self._CONTRIBUTOR_ADDRESS: self.proposal_details[_ipfs_key][
                            self._CONTRIBUTOR_ADDRESS],
                        self._TIMESTAMP: self.progress_report_details[_ipfs_key][_report_key][
                            self._TIMESTAMP],
                        self._IPFS_HASH: self.progress_report_details[_ipfs_key][_report_key][
                            self._IPFS_HASH],
                        self._REPORT_KEY: _report_key,
                        self._IPFS_KEY: _ipfs_key,
                        "approved_votes": _vote_result["approved_votes"],
                        "rejected_votes": _vote_result["rejected_votes"],
                        "total_votes": _vote_result["total_votes"]}
                    _remaining_progress_report.append(_progress_reports_details)

            return _remaining_progress_report

    @external(readonly=True)
    def get_projected_fund(self, _wallet_address: str) -> dict:
        """
        Returns projected fund to be disburse on end of voting period
        :param _wallet_address: wallet address of a contributor or sponsor
        :return: dict of project fund records with total amount to be paid at end of the voting period
        """
        cps_treasury_score = self.create_interface_score(self.cps_treasury_score.get(), CPS_TREASURY_INTERFACE)
        if _wallet_address in self.contributors:
            return cps_treasury_score.get_contributor_projected_fund(_wallet_address)

        if _wallet_address in self.sponsors:
            return cps_treasury_score.get_sponsor_projected_fund(_wallet_address)

    @external
    def update_period(self):
        """
        Update Period after ending of the Allocated BlockTime for each period.
        :return:
        """
        if self.block_height <= self.next_block.get():
            revert(f"Current Block : {self.block_height}, Next Block : {self.next_block.get()}")

        self.set_PReps()
        if self.period_name.get() == "Application Period":
            self.period_name.set("Voting Period")
            self.next_block.set(self.next_block.get() + _BLOCKS_COUNT)
            self.update_application_result()

        else:
            self.period_name.set("Application Period")
            self.next_block.set(self.next_block.get() + _BLOCKS_COUNT)
            self.update_proposals_result()
            self.update_budget_adjustments()
            self.update_progress_report_result()
            self.check_progress_report_submission()
            self.update_denylist_preps()

    def update_application_result(self):
        for x in range(0, len(self._pending)):
            if self._pending[x] not in self.voting_proposals:
                self.voting_proposals.put(self._pending[x])

        for x in range(0, len(self._waiting)):
            if self._waiting[x] not in self.voting_progress_reports:
                self.voting_progress_reports.put(self._waiting[x])

        for x in range(0, len(self._active)):
            if self._active[x] not in self.active_proposals:
                self.active_proposals.put(self._active[x])

        for x in range(0, len(self._paused)):
            if self._paused[x] not in self.active_proposals:
                self.active_proposals.put(self._paused[x])

    def update_proposals_result(self):
        """
        Calculate the votes and update the proposals status on the end of the voting period.
        :return:
        """
        for proposal in range(0, len(self.voting_proposals)):
            proposals = self.voting_proposals.pop()
            _period_count = int(self.proposal_details[proposals][self._PERIOD_COUNT])
            _title = self.proposal_details[proposals][self._PROJECT_TITLE]
            _sponsor_address = self.proposal_details[proposals][self._SPONSOR_ADDRESS]
            _contributor_address = self.proposal_details[proposals][self._CONTRIBUTOR_ADDRESS]
            _total_budget = int(self.proposal_details[proposals][self._BUDGET])

            _voters_list = self.voters_list[proposals][self._VOTERS]
            _voters = _voters_list.split(",")

            _all_preps = self.get_preps_address()
            _not_voters = list(set(self._main_preps) - set(_voters))
            for x in _not_voters:
                if x not in self.inactive_preps:
                    self.inactive_preps.put(x)

            _vote_result = self.get_vote_result(proposals)
            _approve_voters = int(_vote_result["approve_voters"])
            _approved_votes = int(_vote_result["approved_votes"])
            _total_votes = int(_vote_result["total_votes"])
            _total_voters = int(_vote_result["total_voters"])

            if _total_voters == 0 or _total_votes == 0:
                self.proposal_details[proposals][self._STATUS] = self._REJECTED
                self.proposal_details[proposals][self._TIMESTAMP] = str(self.now())
                _data_out = self.proposals_status[self._PENDING].pop()
                if _data_out != proposals:
                    for p in range(0, len(self.proposals_status[self._PENDING])):
                        if self.proposals_status[self._PENDING][p] == proposals:
                            self.proposals_status[self._PENDING][p] = _data_out

                self._rejected.put(proposals)

            elif _approve_voters / _total_voters >= _MAJORITY and _approved_votes / _total_votes >= _MAJORITY:
                self.proposal_details[proposals][self._STATUS] = self._ACTIVE
                self.proposal_details[proposals][self._TIMESTAMP] = str(self.now())
                _data_out = self.proposals_status[self._PENDING].pop()
                if _data_out != proposals:
                    for p in range(0, len(self.proposals_status[self._PENDING])):
                        if self.proposals_status[self._PENDING][p] == proposals:
                            self.proposals_status[self._PENDING][p] = _data_out
                self._active.put(proposals)
                self.sponsors.put(_sponsor_address)

                self.sponsor_deposit[proposals][self._DEPOSIT_STATUS] = "bond_on_hold"

                cpf_treasury_score = self.create_interface_score(self.cpf_score.get(), CPF_TREASURY_INTERFACE)
                cpf_treasury_score.transfer_proposal_fund_to_cps_treasury(proposals, _period_count, _title,
                                                                          _sponsor_address, _contributor_address,
                                                                          _total_budget)

            else:
                self.proposal_details[proposals][self._STATUS] = self._REJECTED
                self.proposal_details[proposals][self._TIMESTAMP] = str(self.now())
                _data_out = self.proposals_status[self._PENDING].pop()
                if _data_out != proposals:
                    for p in range(0, len(self.proposals_status[self._PENDING])):
                        if self.proposals_status[self._PENDING][p] == proposals:
                            self.proposals_status[self._PENDING][p] = _data_out

                _sponsor_address = str(self.sponsor_deposit[proposals][self._SPONSOR_ADDRESS])
                _sponsor_deposit_amount = int(self.sponsor_deposit[proposals][self._DEPOSIT_AMOUNT])

                self.sponsor_deposit[proposals][self._DEPOSIT_STATUS] = "bond_rejected"
                self.icx.transfer(_sponsor_address, _sponsor_deposit_amount)
                self.SponsorBondReturned(self.address, _sponsor_address,
                                         f'{_sponsor_deposit_amount // 10 ** 18} ICX returned to sponsor address.')
                self._rejected.put(proposals)

    def update_progress_report_result(self):
        """
        Calculate votes for the progress reports and update the status and get the Installment and Sponsor
        Reward is the progress report is accepted.
        :return:
        """
        for reports in range(0, len(self.voting_progress_reports)):
            _reports = self.voting_progress_reports.pop()
            _report_result = self.get_progress_report_result(_reports)
            _approve_voters = int(_report_result["approve_voters"])
            _reject_voters = int(_report_result["reject_voters"])
            _approved_votes = int(_report_result["approved_votes"])
            _rejected_votes = int(_report_result["rejected_votes"])
            _total_votes = int(_report_result["total_votes"])
            _total_voters = int(_report_result["total_voters"])

            _ipfs_key = _report_result["data"][0][self._IPFS_KEY]

            if _ipfs_key in self.active_proposals:
                _data_out = self.active_proposals.pop()
                if _data_out != _ipfs_key:
                    for x in range(0, len(self.active_proposals)):
                        if self.active_proposals[x] == _ipfs_key:
                            self.active_proposals[x] = _data_out

            _voters_list = self.report_voters_list[_reports][self._VOTERS]
            _voters = _voters_list.split(",")

            _all_preps = self.get_preps_address()
            _not_voters = list(set(self._main_preps) - set(_voters))
            for x in _not_voters:
                if x not in self.inactive_preps:
                    self.inactive_preps.put(x)

            cps_treasury_score = self.create_interface_score(self.cps_treasury_score.get(), CPS_TREASURY_INTERFACE)
            cpf_treasury_score = self.create_interface_score(self.cpf_score.get(), CPF_TREASURY_INTERFACE)

            if _approve_voters / _total_voters >= _MAJORITY and _approved_votes / _total_votes >= _MAJORITY:
                self.progress_report_details[_ipfs_key][_reports][self._STATUS] = self._APPROVED
                self.progress_report_details[_ipfs_key][_reports][self._TIMESTAMP] = str(self.now())
                _data_out = self.progress_report_status[self._WAITING].pop()
                if _data_out != _reports:
                    for p in range(0, len(self.progress_report_status[self._WAITING])):
                        if self.progress_report_status[self._WAITING][p] == _reports:
                            self.progress_report_status[self._WAITING][p] = _data_out
                self.progress_report_status[self._APPROVED].put(_reports)

                if self.proposal_details[_ipfs_key][self._STATUS] == self._PAUSED:
                    self.proposal_details[_ipfs_key][self._STATUS] = self._ACTIVE
                    self.proposal_details[_ipfs_key][self._TIMESTAMP] = str(self.now())
                    _data_out = self.proposals_status[self._PAUSED].pop()
                    if _data_out != _ipfs_key:
                        for p in range(0, len(self.proposals_status[self._PAUSED])):
                            if self.proposals_status[self._PAUSED][p] == _ipfs_key:
                                self.proposals_status[self._PAUSED][p] = _data_out
                    self._active.put(_ipfs_key)

                cps_treasury_score.send_installment_to_contributor(_ipfs_key)
                cps_treasury_score.send_reward_to_sponsor(_ipfs_key)

            elif _reject_voters / _total_voters >= _MAJORITY and _rejected_votes / _total_votes >= _MAJORITY:
                self.progress_report_details[_ipfs_key][_reports][self._STATUS] = self._REJECTED
                self.progress_report_details[_ipfs_key][_reports][self._TIMESTAMP] = str(self.now())
                _data_out = self.progress_report_status[self._WAITING].pop()
                if _data_out != _reports:
                    for p in range(0, len(self.progress_report_status[self._WAITING])):
                        if self.progress_report_status[self._WAITING][p] == _reports:
                            self.progress_report_status[self._WAITING][p] = _data_out
                self.progress_report_status[self._REJECTED].put(_reports)

                if self.proposal_details[_ipfs_key][self._STATUS] == self._ACTIVE:
                    self.proposal_details[_ipfs_key][self._STATUS] = self._PAUSED
                    self.proposal_details[_ipfs_key][self._TIMESTAMP] = str(self.now())
                    _data_out = self.proposals_status[self._PAUSED].pop()
                    if _data_out != _ipfs_key:
                        for p in range(0, len(self.proposals_status[self._ACTIVE])):
                            if self.proposals_status[self._ACTIVE][p] == _ipfs_key:
                                self.proposals_status[self._ACTIVE][p] = _data_out
                    self._paused.put(_ipfs_key)

                elif self.proposal_details[_ipfs_key][self._STATUS] == self._PAUSED:
                    self.proposal_details[_ipfs_key][self._STATUS] = self._DISQUALIFIED
                    self.proposal_details[_ipfs_key][self._TIMESTAMP] = str(self.now())
                    _data_out = self.proposals_status[self._PAUSED].pop()
                    if _data_out != _ipfs_key:
                        for p in range(0, len(self.proposals_status[self._PAUSED])):
                            if self.proposals_status[self._PAUSED][p] == _ipfs_key:
                                self.proposals_status[self._PAUSED][p] = _data_out
                    self._disqualified.put(_ipfs_key)
                    cps_treasury_score.disqualify_project(_ipfs_key)

                    _sponsor_out = self.sponsors.pop()
                    if _sponsor_out != Address.from_string(self.proposal_details[_ipfs_key][self._STATUS]):
                        for sp in range(0, len(self.sponsors)):
                            if self.sponsors[sp] == _ipfs_key:
                                self.sponsors[sp] = _sponsor_out

                    self.sponsor_deposit[_ipfs_key][self._DEPOSIT_STATUS] = "bond_cancelled"
                    _sponsor_deposit_amount = int(self.sponsor_deposit[_ipfs_key][self._DEPOSIT_AMOUNT])
                    cpf_treasury_score.icx(_sponsor_deposit_amount).return_fund_amount()
                    self.SponsorBondReturned(self.address, self.cpf_score.get(),
                                             f'Project Disqualified. {_sponsor_deposit_amount // 10 ** 18} ICX '
                                             f'returned to CPF Treasury Address.')

            else:
                if self.proposal_details[_ipfs_key][self._STATUS] == self._ACTIVE:
                    self.proposal_details[_ipfs_key][self._STATUS] = self._PAUSED
                    self.proposal_details[_ipfs_key][self._TIMESTAMP] = str(self.now())
                    _data_out = self._active.pop()
                    if _data_out != _ipfs_key:
                        for p in range(0, len(self._active)):
                            if self._active[p] == _ipfs_key:
                                self._active[p] = _data_out
                    self._paused.put(_ipfs_key)

                elif self.proposal_details[_ipfs_key][self._STATUS] == self._PAUSED:
                    self.proposal_details[_ipfs_key][self._STATUS] = self._DISQUALIFIED
                    self.proposal_details[_ipfs_key][self._TIMESTAMP] = str(self.now())
                    _data_out = self.proposals_status[self._PAUSED].pop()
                    if _data_out != _ipfs_key:
                        for p in range(0, len(self.proposals_status[self._PAUSED])):
                            if self.proposals_status[self._PAUSED][p] == _ipfs_key:
                                self.proposals_status[self._PAUSED][p] = _data_out
                    self._disqualified.put(_ipfs_key)
                    cps_treasury_score.disqualify_project(_ipfs_key)

                    _sponsor_out = self.sponsors.pop()
                    if _sponsor_out != Address.from_string(self.proposal_details[_ipfs_key][self._STATUS]):
                        for sp in range(0, len(self.sponsors)):
                            if self.sponsors[sp] == _ipfs_key:
                                self.sponsors[sp] = _sponsor_out

                    self.sponsor_deposit[_ipfs_key][self._DEPOSIT_STATUS] = "bond_cancelled"
                    _sponsor_deposit_amount = int(self.sponsor_deposit[_ipfs_key][self._DEPOSIT_AMOUNT])
                    cpf_treasury_score.icx(_sponsor_deposit_amount).return_fund_amount()
                    self.SponsorBondReturned(self.address, self.cpf_score.get(),
                                             f'Project Disqualified. {_sponsor_deposit_amount // 10 ** 18} ICX '
                                             f'returned to CPF Treasury Address.')

                self.progress_report_details[_ipfs_key][_reports][self._STATUS] = self._REJECTED
                self.progress_report_details[_ipfs_key][_reports][self._TIMESTAMP] = str(self.now())
                _data_out = self.progress_report_status[self._WAITING].pop()
                if _data_out != _reports:
                    for p in range(0, len(self._waiting)):
                        if self._waiting[p] == _reports:
                            self._waiting[p] = _data_out
                self._progress_rejected.put(_reports)

    def check_progress_report_submission(self):
        """
        Check if all active and paused proposals submits the progress report
        :return:
        """
        cps_treasury_score = self.create_interface_score(self.cps_treasury_score.get(), CPS_TREASURY_INTERFACE)
        cpf_treasury_score = self.create_interface_score(self.cpf_score.get(), CPF_TREASURY_INTERFACE)
        for _ipfs_key in self.active_proposals:
            if self.proposal_details[_ipfs_key][self._STATUS] == self._ACTIVE:
                self.proposal_details[_ipfs_key][self._STATUS] = self._PAUSED
                self.proposal_details[_ipfs_key][self._TIMESTAMP] = str(self.now())
                _data_out = self._active.pop()
                if _data_out != _ipfs_key:
                    for p in range(0, len(self._active)):
                        if self._active[p] == _ipfs_key:
                            self._active[p] = _data_out
                self._paused.put(_ipfs_key)

            elif self.proposal_details[_ipfs_key][self._STATUS] == self._PAUSED:
                self.proposal_details[_ipfs_key][self._STATUS] = self._DISQUALIFIED
                self.proposal_details[_ipfs_key][self._TIMESTAMP] = str(self.now())
                _data_out = self.proposals_status[self._PAUSED].pop()
                if _data_out != _ipfs_key:
                    for p in range(0, len(self.proposals_status[self._PAUSED])):
                        if self.proposals_status[self._PAUSED][p] == _ipfs_key:
                            self.proposals_status[self._PAUSED][p] = _data_out
                self._disqualified.put(_ipfs_key)
                cps_treasury_score.disqualify_project(_ipfs_key)

                _sponsor_out = self.sponsors.pop()
                if _sponsor_out != Address.from_string(self.proposal_details[_ipfs_key][self._STATUS]):
                    for sp in range(0, len(self.sponsors)):
                        if self.sponsors[sp] == _ipfs_key:
                            self.sponsors[sp] = _sponsor_out

                self.sponsor_deposit[_ipfs_key][self._DEPOSIT_STATUS] = "bond_cancelled"
                _sponsor_deposit_amount = int(self.sponsor_deposit[_ipfs_key][self._DEPOSIT_AMOUNT])
                cpf_treasury_score.icx(_sponsor_deposit_amount).return_fund_amount()
                self.SponsorBondReturned(self.address, self.cpf_score.get(),
                                         f'Project Disqualified. {_sponsor_deposit_amount // 10 ** 18} ICX '
                                         f'returned to CPF Treasury Address.')

    def update_budget_adjustments(self):
        """
        Update the budget amount and added month time if the budget adjustment application is approved by majority.
        :return:
        """
        for budget in range(0, len(self.budget_approvals_key_list)):
            _budget_key = self.budget_approvals_key_list.pop()
            _ipfs_key = self.budget_voters_list[_budget_key][self._IPFS_KEY]
            _vote_result = self.get_budget_adjustment_vote_result(_budget_key)
            _approve_voters = int(_vote_result["approve_voters"])
            _total_voters = int(_vote_result["total_voters"])
            _approved_votes = int(_vote_result["approved_votes"])
            _total_votes = int(_vote_result["total_votes"])

            if _approve_voters / _total_voters >= _MAJORITY and _approved_votes / _total_votes >= _MAJORITY:
                self.proposal_details[_ipfs_key][self._PERIOD_COUNT] = int(
                    self.proposal_details[_ipfs_key][self._PERIOD_COUNT]) + int(
                    self.progress_report_details[_ipfs_key][_budget_key][self._PERIOD_COUNT])
                self.proposal_details[_ipfs_key][self._BUDGET] = int(
                    self.proposal_details[_ipfs_key][self._BUDGET]) + int(
                    self.progress_report_details[_ipfs_key][_budget_key][self._ADJUSTMENT_AMOUNT])

                cpf_treasury_score = self.create_interface_score(self.cpf_score.get(), CPF_TREASURY_INTERFACE)
                cpf_treasury_score.update_proposal_fund(_ipfs_key, int(
                    self.progress_report_details[_ipfs_key][_budget_key][self._ADJUSTMENT_AMOUNT]), int(
                    self.progress_report_details[_ipfs_key][_budget_key][self._PERIOD_COUNT]))

    def update_denylist_preps(self):
        """
        Add a Registered P-Rep to DenyList is they miss voting on the voting period.
        :return:
        """
        denylist_preps = []
        for x in self.denylist1:
            denylist_preps.append(x)
        for y in self.denylist2:
            denylist_preps.append(y)
        for z in self.denylist3:
            denylist_preps.append(z)
        for x in range(0, len(self.inactive_preps)):
            _prep = self.inactive_preps.pop()
            _data_out = self._main_preps.pop()
            if _data_out != _prep:
                for prep in range(0, len(self._main_preps)):
                    if self._main_preps[prep] == _prep:
                        self._main_preps[prep] = _data_out

            self.denylist.put(_prep)
            if _prep in denylist_preps:
                if _prep in self.denylist1:
                    _prep_out = self.denylist1.pop()
                    if _prep != _prep_out:
                        for prep in range(0, len(self.denylist1)):
                            if self.denylist1[prep] == _prep:
                                self.denylist1[prep] = _prep_out
                    self.denylist2.put(_prep)

                elif _prep in self.denylist2:
                    _prep_out = self.denylist2.pop()
                    if _prep != _prep_out:
                        for prep in range(0, len(self.denylist2)):
                            if self.denylist2[prep] == _prep:
                                self.denylist2[prep] = _prep_out
                    self.denylist3.put(_prep)
            else:
                self.denylist1.put(_prep)

            self.PRepPenalty(Address.from_string(_prep), "P-Rep added to Denylist.")
